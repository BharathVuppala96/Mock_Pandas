import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders=orders[(orders['order_date']>='2019-01-01') & (orders['order_date']<='2019-12-31')]
    orders=orders.groupby(['buyer_id']).agg(orders_in_2019=('order_id','nunique')).reset_index()
    df=users.merge(orders,left_on='user_id',right_on='buyer_id',how='left')
    df=df[['user_id','join_date','orders_in_2019']].fillna(0)
    return df.rename(columns={'user_id':'buyer_id'})