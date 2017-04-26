from pandas_datareader import data
list_a = ['PIH','TURN','FLWS','FCCY','SRCE','VNET','TWOU','JOBS','CAFD','EGHT','AVHI','SHLM','AAON','ABAX','ABEO','ABEOW','ABIL','ABMD','AXAS','ACIU','ACIA','ACTG','ACHC','ACAD','ACST','AXDX','ACCP']

for item in list_a:
    try:
        cache_a = data.DataReader(item,'yahoo','2010-01-01')
        a = 'D:/' + item +'.csv'
        cache_a.to_csv(a)
    except:
        pass


