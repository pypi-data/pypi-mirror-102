import pandas as pd
import numpy as np 


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



    def getRecency(self,matrix,dateFlag):
        """
        Params:
        
            matrix -> data matrix
            dateFlag    ->
        ---------------------
        Output:- entire modified dataframe with the recency feature
        
        """
        matrix['Recency'] = matrix.apply(lambda x: dateFlag - pd.to_datetime(x.order_date),axis =1).dt.days
        
        output = matrix
        
        # Output
        return output




    def getLastOrderValue(self,matrix,train_df):
        """
        Params:
            matrix      ->
            train_df    ->
        --------------------
        Output:
            output = matrix with last order value
        """
        
        target = train_df[train_df.customerid.map(matrix['order_date']) == train_df.order_date][['customerid','totalprice']]
        matrix = matrix.reset_index()
        output = pd.merge(target,matrix,on='customerid')
        output.drop_duplicates(inplace = True)
        
        # Output
        return output




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
        # Get the date which acts as reference point for future calculations
        dateFlag_sep = np.max(org_df['order_date']) - pd.DateOffset(months=timeFlag)
        # Create a grouping aggregator
        grp = train_df.groupby('customerid')

        grp_dict = {'order_date':'max','id':'count','totalprice':'sum','buyeracceptsmarketing':'max','billingaddresscountrycode':'unique'}

        df_matrix = gb.agg(d).rename(columns={'id':'num_orders'})

        df_matrix = self.getRecency(last_orders,dateFlag_sep)

        df_matrix = self.getLastOrderValue(df_matrix,train_df)




        
        output = df_matrix 
        
        return output



# --------------------------------------------------------------------------------------------------------------------------------

    def getMergedDF(self,data_list,key):
        """
        Params: 
            data_list -> list that contains all dataframes
            key - string, the mutual key for the merge. 
        ---------------
        Output: Merged dataset
        
        
        """
        output = reduce(lambda  left,right: pd.merge(left,right,on=[key],
                                                how='outer'), data_list)
        
        
        return output


# ------------------------------------------------------------------------------------------------------------------------------------



    def prepareDF(self,original_dataset,dateFlag_sep,date_flag_min,lag,items_dataset):
        """
        Params:
            original_dataset ->
            timeFlag         ->
            train_window     ->
        -------------------------------__version__
        Output:
        
        """
        
        # First, perform initial cleaning and save a log file of actions
        # df,log_file = getCleanData(original_dataset)
        # Get the first matrices
        train_data = self.getTrainingframe(df,dateFlag_sep,date_flag_min)
        print('train_data Done')
        # For the target values calculations first -> get the relevant dataframe with the relevant timeframe
        target_frame = self.getTargetframe(df,dateFlag_sep,lag)
        print('target frame done')
        # Calculate the target value
        target_value = self.getTargetValues(train_data,target_frame)
        print('target value done')
        # Calculate features
        df = self.getFeaturesMatrix(train_data,orders,lag,items_dataset)
        
        # Merge feature sets
        data = self.getMergedDF(df,'customerid')
        #Merge with target value 
        
        finalDF = pd.merge(data,target_value,on='customerid')
        
        # finalDf = finalDF.rename(columns = {'num_orders':'Num_orders','totalprice':'Total_spent'})
        
        output =  finalDF
        
        
        return output
# -----------------------------------------------------------------------------------------------

    def buildDF(original_dataset,lag,train_window,items_dataset):
        """
        Params:
            original_dataset - > the original raw data 
            lag              - > size ( in months) of the targetValue window
            train_window     - > size (__version__------------
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
        output.append(self.prepareDF(original_dataset,dateFlag_sep,date_flag_min,lag,items_dataset))
        print(dateFlag_sep,date_flag_min)
        # Repeat the procedure until the bottom limit of the trainFrame reaches the minimum date possible according to the original dataset.
        while date_flag_min >= min_date:
        
            dateFlag_sep = dateFlag_sep - pd.DateOffset(months=lag)
            date_flag_min = dateFlag_sep - pd.DateOffset(months=train_window)
            output.append(self.prepareDF(original_dataset,dateFlag_sep,date_flag_min,lag,items_dataset))
            print(dateFlag_sep,date_flag_min)
            
            
        return output