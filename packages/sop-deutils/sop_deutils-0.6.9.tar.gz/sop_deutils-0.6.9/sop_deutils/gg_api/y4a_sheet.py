import re
import logging
import warnings
from typing import Callable
import pandas as pd
import gspread
from ..y4a_credentials import get_credentials

warnings.filterwarnings("ignore", category=UserWarning)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


class GGSheetUtils:
    """
    Utils for Google Sheets

    :param account_name: the client account name for Google Sheet
        defaults to 'da'
    :param auth_dict: the dictionary of user credentials for the Google Sheet,
        defaults to None
        if None, the module will use the default credentials
        of DA team
    """

    def __init__(
        self,
        account_name: str = 'da',
        user_creds: dict = None,
    ) -> None:
        self.account_name = account_name
        self.user_creds = user_creds

    def construct_data(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        df = data.copy()

        for col in df.columns:
            try:
                df[col] = df[col].astype('float')
            except Exception:
                try:
                    pd.to_datetime(df[col])
                    df[col] = df[col].astype('string').apply(
                        lambda x: re.sub('^[0-9]+$', '', x)
                    )
                    df[col] = pd.to_datetime(
                        df[col]
                    ).dt.strftime('%Y-%m-%d').astype('string')
                except Exception:
                    df[col] = df[col].astype('string')

        df.fillna('', inplace=True)

        return df

    def open_spread_sheet(
        self,
        sheet_id: str,
    ) -> Callable:
        if self.user_creds:
            auth_dict = self.user_creds
        else:
            credentials = get_credentials(
                platform='gg_api',
                account_name=self.account_name,
            )

            email = credentials['email']
            private_key = credentials['secret_key']

            auth_dict = {
                'client_email': email,
                'private_key': private_key,
                'token_uri': 'https://oauth2.googleapis.com/token',
            }

            client = gspread.service_account_from_dict(auth_dict)

        spread_sheet = client.open_by_key(
            key=sheet_id,
        )

        return spread_sheet

    def get_work_sheet(
        self,
        spread_sheet: Callable,
        sheet_name: str,
    ) -> Callable:
        work_sheet = spread_sheet.worksheet(sheet_name)

        return work_sheet

    def create_spread_sheet(
        self,
        sheet_name: str,
        folder_id: str = None,
        share_to: list = [],
    ) -> str:
        """
        Create a new spread sheet

        :param sheet_name: name of the sheet
        :param folder_id: id of the folder contains spreadsheet
        :param share_to: list of email to share the spreadsheet
            defaults to []

        :return: the created spreadsheet id
        """

        if self.user_creds:
            auth_dict = self.user_creds
        else:
            credentials = get_credentials(
                platform='gg_api',
                account_name=self.account_name,
            )

            email = credentials['email']
            private_key = credentials['secret_key']

            auth_dict = {
                'client_email': email,
                'private_key': private_key,
                'token_uri': 'https://oauth2.googleapis.com/token',
            }

            client = gspread.service_account_from_dict(auth_dict)

        spread_sheet = client.create(
            title=sheet_name,
            folder_id=folder_id,
        )
        if share_to:
            for mail in share_to:
                spread_sheet.share(
                    email_address=mail,
                    perm_type='user',
                    role='writer',
                )

        return spread_sheet.id

    def list_all_work_sheets(
        self,
        sheet_id: str,
    ) -> list:
        """
        Get all available worksheet of spreadsheet

        :param sheet_id: spreadsheet id

        :return: list all worksheets of spreadsheet
        """

        spread_sheet = self.open_spread_sheet(sheet_id)

        work_sheets = spread_sheet.worksheets()

        return work_sheets

    def delete_work_sheet(
        self,
        sheet_id: str,
        sheet_name: str = 'Sheet1',
    ) -> None:
        """
        Delete specific worksheet of spreadsheet

        :param sheet_id: spreadsheet id
        :param sheet_name: worksheet name
            defaults to 'Sheet1'
        """

        spread_sheet = self.open_spread_sheet(sheet_id)

        work_sheet = self.get_work_sheet(
            spread_sheet=spread_sheet,
            sheet_name=sheet_name,
        )

        spread_sheet.del_worksheet(work_sheet)

    def clear_work_sheet(
        self,
        sheet_id: str,
        sheet_name: str = 'Sheet1',
        delete_cells: bool = False,
    ) -> None:
        """
        Clear all data of specific worksheet of spreadsheet

        :param sheet_id: spreadsheet id
        :param sheet_name: worksheet name
            defaults to 'Sheet1'
        :param delete_cells: whether to delete all cells
            defaults to False
        """

        spread_sheet = self.open_spread_sheet(sheet_id)

        work_sheet = self.get_work_sheet(
            spread_sheet=spread_sheet,
            sheet_name=sheet_name,
        )

        work_sheet.clear()

        if delete_cells:
            work_sheet.delete_columns(2, work_sheet.col_count)
            work_sheet.delete_rows(2, work_sheet.row_count)

    def get_data(
        self,
        sheet_id: str,
        sheet_name: str = 'Sheet1',
        range_from: str = 'A',
        range_to: str = 'Z',
        get_all_data: bool = False,
        columns_first_row: bool = False,
        auto_format_columns: bool = False,
    ) -> pd.DataFrame:
        """
        Get data from the given sheet

        :param sheet_id: spreadsheet name
        :param sheet_name: worksheet name
            defaults to 'Sheet1'
        :param range_from: the begining of the range
            of data from sheet to get
            defaults to 'A'
        :param range_to: the end of the range
            of data from sheet to get
            defaults to 'Z'
        :param get_all_data: whether to get all data of the worksheet
            defaults to False
        :param columns_first_row: whether to convert the first row
            to columns
            defaults to False
        :param auto_format_columns: whether to format columns name
            of the dataframe
            defaults to False

        :return: the dataframe contains data from sheet
        """

        spread_sheet = self.open_spread_sheet(sheet_id)

        data_range = f'{range_from}:{range_to}'
        if get_all_data:
            data_range = sheet_name
        else:
            data_range = f'{sheet_name}!{data_range}'

        data = spread_sheet.values_get(data_range)['values']
        df = pd.DataFrame(data)
        if columns_first_row:
            df.columns = df.iloc[0].to_list()
            df = df.iloc[1:].reset_index(drop=True)
        if auto_format_columns:
            if columns_first_row:
                formatted_cols = list()
                for col in df.columns:
                    if not col:
                        col = ''
                    col = str(col).lower()
                    col = re.sub(r'[^\w]+', '_', col)
                    col = re.sub(r'^_', '', col)
                    col = re.sub(r'_$', '', col)
                    formatted_cols.append(col)
                df.columns = formatted_cols
            else:
                raise ValueError(
                    'Can not format column names when '
                    'the value of param `columns_first_row` is False'
                )

        return df

    def insert_data(
        self,
        data: pd.DataFrame,
        sheet_id: str,
        sheet_name: str = 'Sheet1',
        from_row_index: int = 1,
        insert_column_names: bool = False,
    ) -> None:
        """
        Insert data to the given sheet

        :param data: dataframe contains data to insert
        :param sheet_id: spreadsheet id
        :param sheet_name: worksheet name
            defaults to 'Sheet1'
        :param from_row_index: the index of the row
            beginning to insert
            defaults to 1
        :param insert_column_names: whether to insert column names
            defaults to False
        """

        spread_sheet = self.open_spread_sheet(sheet_id)

        work_sheet = self.get_work_sheet(
            spread_sheet=spread_sheet,
            sheet_name=sheet_name,
        )

        constructed_data = self.construct_data(data)
        data_values = constructed_data.values.tolist()

        if insert_column_names:
            col_values = [data.columns.to_list()]
            work_sheet.insert_rows(
                col_values,
                row=from_row_index,
            )
            work_sheet.insert_rows(
                data_values,
                row=from_row_index+1,
            )
        else:
            work_sheet.insert_rows(
                data_values,
                row=from_row_index,
            )

    def update_data(
        self,
        data: pd.DataFrame,
        sheet_id: str,
        sheet_name: str = 'Sheet1',
        range_from: str = 'A1',
    ) -> None:
        """
        Update data of the given sheet

        :param data: dataframe contains data to update
        :param sheet_id: spreadsheet name
        :param sheet_name: worksheet name
            defaults to 'Sheet1'
        :param range_from: the begining of the range
            of data from sheet to update
            defaults to 'A1'
        """

        spread_sheet = self.open_spread_sheet(sheet_id)

        work_sheet = self.get_work_sheet(
            spread_sheet=spread_sheet,
            sheet_name=sheet_name,
        )

        constructed_data = self.construct_data(data)
        data_values = constructed_data.values.tolist()

        num_current_rows = work_sheet.row_count
        num_current_cols = work_sheet.col_count

        range_from_index = gspread.utils.a1_to_rowcol(range_from)
        row_from_index = range_from_index[0]
        col_from_index = range_from_index[-1]

        if row_from_index > num_current_rows:
            rows_to_resize = row_from_index
        else:
            rows_to_resize = num_current_rows

        if col_from_index > num_current_cols:
            cols_to_resize = col_from_index
        else:
            cols_to_resize = num_current_cols

        work_sheet.resize(
            rows=rows_to_resize,
            cols=cols_to_resize,
        )

        work_sheet.update(
            f'{range_from}',
            data_values,
        )

    def remove_data(
        self,
        sheet_id: str,
        sheet_name: str = 'Sheet1',
        list_range: list = [
            'A1:Z1',
            'A4:Z4',
        ],
    ) -> None:
        """
        Remove data from specific range of the given sheet

        :param sheet_id: spreadsheet name
        :param sheet_name: worksheet name
            defaults to 'Sheet1'
        :param list_range: list of data ranges to remove
            defaults to ['A1:Z1', 'A4:Z4']
        """

        spread_sheet = self.open_spread_sheet(sheet_id)

        work_sheet = self.get_work_sheet(
            spread_sheet=spread_sheet,
            sheet_name=sheet_name,
        )
        work_sheet.batch_clear(list_range)
