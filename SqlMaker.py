import pypyodbc as p
from ldap3 import Server,Connection,ALL, NTLM

def ResultIter(cursor, arraysize=100):
    while True:
        row = cursor.fetchmany(arraysize)
        if not row:
            break
        for result in row:
            yield result


def connect(Query):
    # db connection
    server = 'pbapclu'
    database = 'Reporting'
    connStr = (r'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';' + 'Trusted_Connection=yes')
    conn = p.connect(connStr)
    dbCursor = conn.cursor()
    dbCursor.execute(Query)

    rowCounter = 1
    stringResult = None
    resultArray = []

    for result in ResultIter(dbCursor):
        stringResult = str(result)
        resultArray.append(stringResult)
    conn.close()
    return(resultArray)





class SqlMaker(object):
    def __init__(self,user,cusips= None):
        self.user = user
        if cusips is None:
            self.cusips = []
        else:
            self.cusips = cusips
        self.owner = []
        self.repIDS = []

    def findOwner(self):
        sqlString = """select x.[Owner ID] from (
                    SELECT 
                    CASE 
                    WHEN CHARINDEX('@',Salespersoneemail) > 0 then 
                        REPLACE(SUBSTRING(Salespersoneemail,1,CHARINDEX('@',Salespersoneemail)),'@','')
                    WHEN CHARINDEX('@',Salespersoneemail) < 0 then
                    Salespersoneemail
                    END as userid,
                    SalespersonID,[Owner ID] from dw.dbo.vtsSalesPersonAll a
                    left join reporting.dm.SalesPersonOwnerMap o on o.[SalesPerson ID] = a.SalespersonID) x 
                    where x.userid = '%s'""" %self.user
        return sqlString

    def findTrades(self):
        l = ['31362QGC7', '31362L4R8', '31362L4R8', '31362GM57', '31362GM57']
        l = tuple(l)
        print(l)
        params = {'l':l}
        sqlString = """select * from reporting.dm.vTradesSalesPerson ts where ts.[Rep ID] in ('138')
                     and ts.cusip in %(l)s""" %  l
        return sqlString

CUSIPS = ['31362QGC7','31362L4R8','31362L4R8','31362GM57','31362GM57']




# a = connect(SqlMaker('jmercurio',CUSIPS).findOwner())
#
# b = []
# for num in a:
#     b.append(num.replace(',)','',-1).replace('(','',-1))
#
# print(b)

# print(SqlMaker('jmercurio',CUSIPS).findTrades())
#a = connect(SqlMaker('jmercurio',CUSIPS).findTrades())

# b = []
# for num in a:
#     b.append(num)

#print(b)



#DBConnecT(SqlMaker.findOwner())

l = ['31362QGC7', '31362L4R8', '31362L4R8', '31362GM57', '31362GM57']
l = tuple(l)
print(l)
params = {'l': l}
sqlString = """select * from reporting.dm.vTradesSalesPerson ts where ts.[Rep ID] in ('138')
                 and ts.cusip in %(l)s""" % l

