from copy import deepcopy
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient  # 代码提示
from arts.vtype import uniset, empset, SysEmpty, ToolPool, OrmIndexError
from arts.mongo._core import Factory, containAll, containAny, containNo, isin, notin, re
from arts.mongo._core import Filter, mc, makeSlice, allColumns, upList, mup


repairUpsert = False
# pymongo官方bug
# cannot infer query fields to set, path 'a' is matched twice, full error: {'index': 0, 'code': 54, 'errmsg': "cannot infer query fields to set, path 'a' is matched twice"}

class sheetORM():
    _variable = True

    def __init__(self, connPool:ToolPool, dbName:str, sheetName:str, where=None, columns=allColumns, _sort=None):
        assert columns
        self.connPool = connPool
        self.dbName = dbName
        self.sheetName = sheetName
        self.where = where or Factory(uniset)
        self.columns = columns  # str型 或 tuple型 或 allColumns, 都是不可变的
        self._sort = deepcopy(_sort or {})
            # {A:True, B:False, C:1, D:0}
            # bool(value) == True 表示升序
            # bool(value) == False 表示降序
        self._variable = False

    def __setattr__(self, name, value):
        assert self._variable
        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        conn:MongoClient = self.connPool.get()
        return conn[self.dbName][self.sheetName].__getattribute__(name)

    def __repr__(self):
        return f'coolmongo.sheetORM("{self.dbName}.{self.sheetName}")'
    __str__ = __repr__

    def _copy(self, where=SysEmpty, columns=SysEmpty, _sort=SysEmpty):
        return sheetORM(
            connPool = self.connPool,
            dbName = self.dbName,
            sheetName = self.sheetName,
            where = self.where if where is SysEmpty else where,
            columns = self.columns if columns is SysEmpty else columns,
            _sort = self._sort if _sort is SysEmpty else _sort
        )

    def _ParseColumns(self):
        cols = self.columns
        if cols is allColumns: return None
        if isinstance(cols, tuple):
            cols = dict.fromkeys(cols, 1)
        else:
            cols = {cols:1}
        cols.setdefault('_id', 0)
        return cols

    def order(self, **rule): return self._copy(_sort={**rule})

    def _ParseOrder(self):
        if self._sort:
            return [(k, 1 if v else -1) for k,v in self._sort.items()]
        return []
    
    def insert(self, data):
        conn:MongoClient = self.connPool.get()
        sheet = conn[self.dbName][self.sheetName]
        if type(data) is dict:
            future = sheet.insert_one(data)
            # r = await sheet.insert(data)
            # r.inserted_id
        else:
            future = sheet.insert_many(data)
            # r = await sheet.insert([line1, line2])
            # r.inserted_ids
        self.connPool.put(conn)
        return future

    def delete(self):
        return makeSlice(self._deleteBase)

    async def _deleteBase(self, key):
        conn:MongoClient = self.connPool.get()
        sheet = conn[self.dbName][self.sheetName]
        # [::]
        if isinstance(key, slice):
            L, R, S = key.start, key.stop, key.step or 1
            if S in [None,1]:
                if (L in [None,1] and R in [None,-1]) or (L == -1 and R == 1):
                    r = await sheet.delete_many(ParseWhere(self))
                    self.connPool.put(conn)
                    return r
                    # r.acknowledged, r.deleted_count
        # [1]且无排序
        if key == 1 and not self._ParseOrder():
            r = await sheet.delete_one(ParseWhere(self))
            self.connPool.put(conn)
            return r
            # r.acknowledged, r.deleted_count
        # 其它情况
        try:
            ids = await self['_id'][key]
        except OrmIndexError:
            condition = Factory(empset).ParseWhere()
            r = await sheet.delete_one(condition)
            self.connPool.put(conn)
            return r
        else:
            if isinstance(ids, list):
                condition = (mc._id == isin(*ids)).ParseWhere()
                r = await sheet.delete_many(condition)
                self.connPool.put(conn)
                return r
            else:
                condition = (mc._id == ids['_id']).ParseWhere()
                r = await sheet.delete_one(condition)
                self.connPool.put(conn)
                return r

    def update(self, data:dict=None):
        return makeSlice(self._updateBase, data=data, default=None)
    
    async def _updateBase(self, key, data=None, default=None):
        data_ = {'$set':{}}
        for k,v in (data or {}).items():
            if isinstance(v, upList):
                data_.setdefault(v.name, {})[k] = v.value
            else:
                data_['$set'][k] = v
        conn:MongoClient = self.connPool.get()
        sheet = conn[self.dbName][self.sheetName]
        empsetCondi = Factory(empset).ParseWhere()
        # [::]
        if isinstance(key, slice):
            L, R, S = key.start, key.stop, key.step or 1
            if S in [None,1]:
                if (L in [None,1] and R in [None,-1]) or (L == -1 and R == 1):
                    r = await sheet.update_many(ParseWhere(self), data_)
                    if repairUpsert and not r.matched_count and default:
                        r = await sheet.update_many(empsetCondi, {'$setOnInsert':default}, upsert=True)
                    self.connPool.put(conn)
                    return r
                    # r.acknowledged, r.matched_count
                    # matched_count 与 modified_count 的区别:
                    ## matched_count 表示匹配到的数目, 如果是update_one, 则 matched_count in [0, 1]
                    ## modified_count 表示数据有变化的数目
                    ## 如果一条数据修改前和修改后一致(例如:把3修改成3), 则不会统计到modified_count中
        # [1]且无排序
        if key == 1 and not self._ParseOrder():
            r = await sheet.update_one(ParseWhere(self), data_)
            if repairUpsert and not r.matched_count and default:
                r = await sheet.update_one(empsetCondi, {'$setOnInsert':default}, upsert=True)
            self.connPool.put(conn)
            return r
            # r.acknowledged, r.matched_count
        # 其它情况
        try:
            ids = await self['_id'][key]
        except OrmIndexError:
            if repairUpsert and default:
                r = await sheet.update_one(empsetCondi, {'$setOnInsert':default}, upsert=True)
            else:
                r = await sheet.update_one(empsetCondi, {'$set':{}})
            self.connPool.put(conn)
            return r
        else:
            if isinstance(ids, list):
                if ids:
                    ids = [x['_id'] for x in ids]
                    condition = (mc._id == isin(*ids)).ParseWhere()
                    r = await sheet.update_many(condition, data_)
                    self.connPool.put(conn)
                    return r
                else:
                    if repairUpsert and default:
                        r = await sheet.update_many(empsetCondi, {'$setOnInsert':default}, upsert=True)
                    else:
                        r = await sheet.update_many(empsetCondi, {'$set':{}})
                    self.connPool.put(conn)
                    return r
            else:
                condition = (mc._id == ids['_id']).ParseWhere()
                r = await sheet.update_one(condition, data_)
                self.connPool.put(conn)
                return r
    
    async def len(self):
        conn:MongoClient = self.connPool.get()
        sheet = conn[self.dbName][self.sheetName]
        tatal = await sheet.count_documents(ParseWhere(self))
        self.connPool.put(conn)
        return tatal
    
    def get(self, index, default=None):
        try:
            return self[index]
        except IndexError:
            return default

    async def _find_one(self, key):
        index = key
        if index < 0: index = await self.len() + index + 1
        if index < 1: raise OrmIndexError(f"index({key}) out of range")
        skip = index - 1
        conn:MongoClient = self.connPool.get()
        sheet = conn[self.dbName][self.sheetName]
        sh = sheet.find(ParseWhere(self), self._ParseColumns())
        if sort:= self._ParseOrder():
            sh = sh.sort(sort)
        if skip: sh = sh.skip(skip)
        r = await sh.limit(1).to_list(1)
        self.connPool.put(conn)
        if r:
            return r[0]
        else:
            raise OrmIndexError(f"index({key}) out of range")
            # 没有的话引发OrmIndexError错误. 已被self.update和self.delete调用

    async def _find_many(self, key):
        # 没有的话返回空列表, 但不要报错. 已被self.update和self.delete调用
        L, R, S = key.start, key.stop, key.step or 1
        tL, tR, tS = type(L), type(R), type(S)
        assert {tL, tR, tS} <= {int, type(None)}
        assert 0 not in (L, R)
        assert S > 0
        lenSheet = float('inf')
        if '-' in f"{L}{R}":  # -是负号
            lenSheet = await self.len()
            if '-' in str(L): L = lenSheet + L + 1  # R索引
            if '-' in str(R): R = lenSheet + R + 1  # R索引
        sliceSort = True  # 正序
        if tL is tR is int and R < L:
            L, R = R, L
            sliceSort = False  # 逆序
        skip = max(1, L or 1) - 1  # 把L转化成skip
        if R is None: R = float('inf')
        size = R - skip
        if skip >= lenSheet: return []
        if size > 0:
            conn:MongoClient = self.connPool.get()
            sheet = conn[self.dbName][self.sheetName]
            sh = sheet.find(ParseWhere(self), self._ParseColumns())
            if sort:= self._ParseOrder():
                sh = sh.sort(sort)
            if skip: sh = sh.skip(skip)
            if isinstance(size, int): sh = sh.limit(size)
            r = [x async for x in sh]
            self.connPool.put(conn)
            if sliceSort:
                if S == 1:
                    return r
                else:
                    return r[::S]
            else:
                return r[::-S]
        else:
            return []
    
    def __getitem__(self, key):
        # 索引取值
        if isinstance(key, int):
            return self._find_one(key)
        # 切片取值
        if isinstance(key, slice):
            return self._find_many(key)
        # 限定columns
        # 输入多个字符串, 用逗号隔开, Python会自动打包成tuple
        if isinstance(key, (str, tuple)) or key is allColumns:
            return self._copy(columns=key)
        # Factory
        if isinstance(key, Factory):
            return self._copy(where=self.where & key)
        raise TypeError(key)

def ParseWhere(obj:sheetORM):
    return obj.where.ParseWhere()

class dbORM():
    def __init__(self, connPool:ToolPool, dbName):
        self.connPool = connPool
        self.dbName = dbName

    def __getattr__(self, name):
        conn:MongoClient = self.connPool.get()
        return conn[self.dbName].__getattribute__(name)

    def __repr__(self):
        return f'coolmongo.dbORM("{self.dbName}")'
    __str__ = __repr__

    async def getSheetNames(self):
        conn:MongoClient = self.connPool.get()
        sheets = await conn[self.dbName].list_collection_names()
        self.connPool.put(conn)
        return sheets
    
    async def len(self): return len(await self.getSheetNames())

    async def delete_all_sheets(self):
        conn:MongoClient = self.connPool.get()
        db = conn[self.dbName]
        r = [await db.drop_collection(name) for name in db.list_collection_names()]
        self.connPool.put(conn)
        return r

    async def delete_sheets(self, *names):
        conn:MongoClient = self.connPool.get()
        db = conn[self.dbName]
        r = [await db.drop_collection(name) for name in names]
        self.connPool.put(conn)
        return r

    def __getitem__(self, key):
        if isinstance(key, str):
            return sheetORM(connPool=self.connPool, dbName=self.dbName, sheetName=key)
        elif isinstance(key, tuple):
            return [sheetORM(connPool=self.connPool, dbName=self.dbName, sheetName=x) for x in key]
        elif isinstance(key, slice):
            assert key.start is key.stop is key.step is None
            sheets = self.getSheetNames()
            return [sheetORM(connPool=self.connPool, dbName=self.dbName, sheetName=x) for x in sheets]
        else:
            raise TypeError(key)

class ORM():
    def __init__(self, mkconn):
        self.connPool = ToolPool(mktool=mkconn, minlen=1, maxlen=1)
        # 当增删改查报错时, conn不再放回连接池, 以避免含有残留数据

    def __getattr__(self, name):
        conn:MongoClient = self.connPool.get()
        return conn.__getattribute__(name)
    
    async def getDbNames(self):
        conn:MongoClient = self.connPool.get()
        dbs = await conn.list_database_names()
        self.connPool.put(conn)
        return dbs
    
    async def len(self): return len(await self.getDbNames())

    async def delete_all_dbs(self):
        conn:MongoClient = self.connPool.get()
        dbs:list = conn.list_database_names()
        try:
            dbs.remove('admin')
        except:
            pass
        r = [await conn.drop_database(dbName) for dbName in dbs]
        self.connPool.put(conn)
        return r

    async def delete_dbs(self, *names):
        conn:MongoClient = self.connPool.get()
        r = [await conn.drop_database(dbName) for dbName in names]
        self.connPool.put(conn)
        return r

    def __getitem__(self, key):
        if isinstance(key, str):
            return dbORM(connPool=self.connPool, dbName=key)
        elif isinstance(key, tuple):
            return [dbORM(connPool=self.connPool, dbName=x) for x in key]
        elif isinstance(key, slice):
            assert key.start is key.stop is key.step is None
            return [dbORM(connPool=self.connPool, dbName=x) for x in self.getDbNames()]
        else:
            raise TypeError(key)