# something something


class Crp:
    """
    """

    def getTrainingframe(self,df,dateFlag_sep,date_flag_min):
        """
        Params:
            df                -> Dataframe
            dateFlag_sep      -> Timestamp separator
            date_flag_min     -> Min date for training frame
        ---------------------
        Output:
        """
    #     dateFlag_sep = np.max(df['order_date']) - pd.DateOffset(months=timeFlag)
    #     date_flag_min = dateFlag_sep - pd.DateOffset(months=train_window)
        
        df = df[(df.order_date <= dateFlag_sep) & (df.order_date >= date_flag_min)]
        
        return df 


    def getTargetframe(self,df,dateFlag_sep,lag):
        """
        Params:
            df           -> dataframe
            dateFlag_sep -> 
            lag          ->
        --------------------
        Output:
        
        
        """
    #     dateFlag_sep = np.max(df['order_date']) - pd.DateOffset(months=timeFlag)
        date_max = dateFlag_sep + pd.DateOffset(months=lag)
        df = df[(df.order_date > dateFlag_sep) & (df.order_date < date_max)]
        
        return df

# --------------------------------------------------------------------------------------------------------------------------