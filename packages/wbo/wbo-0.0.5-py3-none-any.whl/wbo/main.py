import lxml
import pandas as pd
from datetime import datetime as dt
import os
import plotly.graph_objects as go
import plotly
import tempfile
from time import sleep



class wbo:
    
    def __init__(self,url="https://www.boxofficemojo.com/year/world/"):
        self.url=url
        
    """
    This function takes in min_year (earliest year of data you want) and max_year (latest year of data you want)
    as parameters and uses pd.read_html function to scrape the html table from the box office mojo's page and
    convert it into a dataframe.
    """
    
    def collect_bom(self, min_year=2019, max_year=2021):
        
        years=list(range(min_year, max_year+1))
        df2 = pd.DataFrame()
        
        for i in years:
            url = self.url +f"{i}/"
            print(f"Collecting data for {i}")
            df = pd.read_html(url)
            dfn = df[0]
            dfn['year']=i
            df2 = pd.concat([df2,dfn],axis=0)
            
        df2.rename(columns={'Rank':'rank',"Release Group":'movie_name','Worldwide':'worldwide_gross',
                  'Domestic':'domestic_gross','%':'domestic_perc','Foreign':'foreign_gross',
                  '%.1':'foreign_perc'},inplace=True)
        
        df2.reset_index(inplace=True,drop=True)
        df2.drop(['domestic_perc','foreign_perc','rank'],axis=1,inplace=True)
        
        gross_columns = ['worldwide_gross','domestic_gross','foreign_gross']
        for j in gross_columns:
            df2[j]=df2[j].str.replace(',','',regex=False).str.replace(
                '$','',regex=False).str.replace(r'^-$','0',regex=True).astype(float)
            
        df2['domestic_perc']= ((df2['domestic_gross']/df2['worldwide_gross'])*100).round(2)
        df2['foreign_perc']= ((df2['foreign_gross']/df2['worldwide_gross'])*100).round(2)
        df2['year']=df2['year'].astype(str)
        
        print("Data Collection Compelete!")
        self.d = df2.copy()
        return self.d

    def get_top_movies(self,column='worldwide_gross',number=10):
        
        self.d2 = self.d.sort_values([column],ascending=[False])
        self.d3=self.d2.head(10)
        
        return self.d3
    
    def plot_gross_scatter(self,x='worldwide_gross',y='domestic_gross',text='hovertext',size='domestic_perc'):
        
        def custom_hover(year, worldwide_gross, domestic_gross, foreign_gross):
            return """Year: {}<br>Worldwide: {} $<br>Domestic: {} $<br>Foreign: {} $
            """.format(year, worldwide_gross, domestic_gross, foreign_gross)
        
        d3 = self.d3.copy()
        d3['hovertext'] = d3.apply(lambda x: custom_hover(
            x['year'],
            x['worldwide_gross'],
            x['domestic_gross'],
            x['foreign_gross']
        ), axis = 1)
        
        fig1 = go.Figure()

        for i in d3.movie_name.unique():
            ndf = d3.query('movie_name == @i')

            fig1.add_trace(
                go.Scatter(
                        x=ndf[x],
                        y=ndf[y],
                        text=ndf[text],
                        hovertemplate="<b>"+i+"</b><br><extra></extra>%{text}",
                        mode = 'markers',
                        opacity = 1,
                        name = i,
                        marker=dict(size=ndf[size])
                        )     
                )

        m=fig1.update_layout(

            xaxis={'titlefont':{'color':'#858585'},'linecolor':'#000000',
                   'tickfont':{'color':'#858585','size':18},'showgrid':False},

            yaxis={'titlefont':{'color':'#858585','size':20}, 'tickfont':{'color':'#858585','size':18},
                   'showgrid':False},
            margin={'l': 80, 'b': 40, 't': 30, 'r': 40},
            title={'text': None},#, 'font':{'color':'#2c4a91', 'size':26},'yanchor':"top",'xanchor':"left",'y':.98,'x':.01},
#             legend={'font':{'size':14, 'color':'#333'},'yanchor':"middle",'xanchor':"right",'y':.5,'orientation':'v',
#                     'font':{'size':16,'color':'#000000'}},
            template = 'none',
            #legend_title_text='',
            hovermode='closest',
            width = 1850,
            height = 950,
            showlegend =  True
        )

        temp_file = tempfile.NamedTemporaryFile(suffix = '.html')
        
        s = plotly.offline.plot(m, filename=temp_file.name, auto_open=True)

if __name__ == '__main__':
    pass