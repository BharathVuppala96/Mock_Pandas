import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df= sales[(sales['sale_date']>='2019-01-01') & (sales['sale_date']<='2019-03-31')]
    df1=sales[ (sales['sale_date']>'2019-03-31') | (sales['sale_date']<'2019-01-01')]
    df=df[~df['product_id'].isin(df1['product_id'])]
    product=product[(product['product_id']).isin(df['product_id'])]
    return product[['product_id','product_name']]
   
    


    