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

#--------------------------------------------------------------------------------------------------------------------------

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

    def getTargetValues(self,rain_data,target_data):
        """
        Params:
            train_data  ->
            target_data ->
        --------------------
        Output:
        
        """
        target = []
        customers_id = train_data['customerid'].unique()
        for c_id in customers_id:
            if c_id in target_data['customerid'].unique():
                value = 1
            else:
                value = 0
            target.append([c_id,value])
            
            
        target = pd.DataFrame(target,columns = ['customerid','is_returned'])
        #Output
        return target

 #---------------------------------------------------------------------------------------------------------------------------

    def getFeaturesMatrix(train_df,org_df,timeFlag,items_dataset):
        """
        Params:
            train_df -> train timeframe dataframe
            org_df   -> original dataframe with the all the needed data
            timeFlag -> date separator ( between the traget period and the train period)
        ----------------
        Output: Features Matrix of the chosen timeframe
        
        """
        
        # Get customer ids
        customers = train_df['customerid'].unique()
        
        Crp
        
        
        return output

    def prepareDF(self,original_dataset,dateFlag_sep,date_flag_min,lag,items_dataset):
        """
        Params:
            original_dataset ->
            timeFlag         ->
            train_window     ->
        -------------------------------
        Output:
        
        """
        
        # First, perform initial cleaning and save a log file of actions
        # df,log_file = getCleanData(original_dataset)
        # Get the first matrices
        train_data = self.getTargetframe(df,dateFlag_sep,date_flag_min)
        print('train_data Done')
        # For the target values calculations first -> get the relevant dataframe with the relevant timeframe
        target_frame = getTargetframe(df,dateFlag_sep,lag)
        print('target frame done')
        # Calculate the target value
        target_value = getTargetValues(train_data,target_frame)
        print('target value done')
        # Calculate features
        df = getFeaturesMatrix(train_data,orders,lag,items_dataset)
        
        # Merge feature sets
        data = getMergedDF(df,'customerid')
        
        #Merge with target value 
        
        finalDF = pd.merge(data,target_value,on='customerid')
        
        finalDf = finalDF.rename(columns = {'num_orders':'Num_orders','totalprice':'Total_spent'})
        
        output =  finalDF
        
        
        return output
# -----------------------------------------------------------------------------------------------

    def buildDF(original_dataset,lag,train_window,items_dataset):
        """
        Params:
            original_dataset - > the original raw data 
            lag              - > size ( in months) of the targetValue window
            train_window     - > size ( in months ) of the Feature Matrix window 
            
        -------------------------------------------
        Output: Constructed dataframe 
        
        """
        
        # Lower limit date
        min_date = np.min(original_dataset['order_date']) + pd.DateOffset(months = train_window)
        print('Min date for training timeframe:',min_date)
        output = []
        # Upper limit date
        date_max = np.max(original_dataset['order_date'])
        # Initial relative timeFlag
        dateFlag_sep = date_max - pd.DateOffset(months=lag)
        # Initial timeframe min date
        date_flag_min = dateFlag_sep - pd.DateOffset(months=train_window)
        print(dateFlag_sep,date_flag_min)
        # Construct dataframe according to that timeframe
        output.append(prepareDF(original_dataset,dateFlag_sep,date_flag_min,lag,items_dataset))
        print(dateFlag_sep,date_flag_min)
        # Repeat the procedure until the bottom limit of the trainFrame reaches the minimum date possible according to the original dataset.
        while date_flag_min >= min_date:
        
            dateFlag_sep = dateFlag_sep - pd.DateOffset(months=lag)
            date_flag_min = dateFlag_sep - pd.DateOffset(months=train_window)
            output.append(prepareDF(original_dataset,dateFlag_sep,date_flag_min,lag,items_dataset))
            print(dateFlag_sep,date_flag_min)
            
            
        return output