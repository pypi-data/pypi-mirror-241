import requests
import pandas as pd

class DatasetRetriever:
    """
    DatasetRetriever class to fetch and merge data from various APIs.

    Attributes:
    BASE_URL (str): Base endpoint for API requests.
    API_CODE_MAP (dict): A dictionary mapping API codes to their respective parameters.
    """

    BASE_URL = 'https://ei1d8iyqd3.execute-api.us-east-1.amazonaws.com/BenAI/database'

    # Mapping for API codes to their respective file_name and column_name
    API_CODE_MAP = {
        '102': {'file_name': 'demand', 'column_name': 'Ontario_Demand'},
        '101': {'file_name': 'demand', 'column_name': 'Market_Demand'},
        '103': {'file_name': 'price', 'column_name': 'HOEP'},
        '105': {'file_name': 'demand_5mins', 'column_name': 'Ontario_Demand_5m'},
        '104': {'file_name': 'demand_5mins', 'column_name': 'Market_Demand_5m'}
    }

    def __init__(self):
        """Initialize DatasetRetriever class."""
        pass

    def get_data(self, start_date, end_date, api_code):
        """
        Fetch data from the API based on given parameters.

        Args:
        start_date (str): Start date for the data request.
        end_date (str): End date for the data request.
        api_code (str): Code that maps to specific API parameters.

        Returns:
        dict: Response data from the API.
        """
        if api_code not in self.API_CODE_MAP:
            raise ValueError(f"Invalid API code: {api_code}")

        params = {
            'start_date': start_date,
            'end_date': end_date,
            'file_name': self.API_CODE_MAP[api_code]['file_name'],
            'column_name': self.API_CODE_MAP[api_code]['column_name']
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code

        return response.json()  # Assuming the API returns data in JSON format

    def parse_time(self, df, api_code):
        """
        Parse the 'Time' column for APIs 104 and 105.

        Args:
        df (DataFrame): DataFrame to be parsed.
        api_code (str): API code to check if parsing is needed.

        Returns:
        DataFrame: DataFrame with 'Date' and 'Hour' columns.
        """
        if api_code in ['104', '105']:
            df['Time'] = pd.to_datetime(df['Time'])
            df['Date'] = df['Time'].dt.date
            df['Hour'] = df['Time'].dt.strftime('%H:%M')
            df = df.drop(columns=['Time'])
        return df

    def get_dataframe(self, start_date, end_date, *api_codes):
        """
        Fetch data from multiple APIs and merge them into a single DataFrame.

        Args:
        start_date (str): Start date for the data request.
        end_date (str): End date for the data request.
        *api_codes (str): Variable length argument list of API codes.

        Returns:
        DataFrame: Merged data from all specified APIs.
        """
        dfs = []  # list to store individual dataframes

        for api_code in api_codes:
            data = self.get_data(start_date, end_date, api_code)
            if 'data' in data:  # Ensure the "data" key exists in the JSON response
                df = pd.DataFrame(data['data'])
                df = self.parse_time(df, api_code)  # Parse time if necessary
                print(f'Data for {self.API_CODE_MAP[api_code]["file_name"]}/{self.API_CODE_MAP[api_code]["column_name"]} is retrieved.')
                dfs.append(df)

        # Merging datasets based on 'Date' and 'Hour' columns
        merged_df = dfs[0]
        for df in dfs[1:]:
            merged_df = pd.merge(merged_df, df, on=['Date', 'Hour'], how='outer')

        print('Your merged data is now ready!')
        merged_df['Date'] = pd.to_datetime(merged_df['Date'])
        merged_df = merged_df.sort_values(by=['Date', 'Hour'], ascending=[True, True])
        column_order = ['Date', 'Hour'] + [col for col in merged_df.columns if col not in ['Date', 'Hour']]
        return merged_df[column_order]

# Usage
if __name__ == '__main__':
    retriever = DatasetRetriever()
    final_df = retriever.get_dataframe('2023-11-09', '2023-11-17', '104', '105')
    print(final_df)