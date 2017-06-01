# -*- coding: utf-8 -*-
"""从xls中获取参数化数据，返回列表

For example:

    Data file like this:

    person.xls :

        | id | name | mobile | address  |
        | 01 | Jack | 532223 | USA N.Y. |
        | 02 | Rose | 425368 | JPN S.Y. |
        | 03 | Lily | 808858 | CHN B.J. |

    Code:

        person = ReadXls('person.xls')
        print person.data

    Result(in one line):

        [{'id':'01', 'name':'Jack', 'mobile': '532223', 'address':'USA N.Y.'},
        {'id':'02', 'name':'Rose', 'mobile': '425368', 'address':'JPN S.Y.'},
        {'id':'03', 'name':'Lily', 'mobile': '808858', 'address':'CHN B.J.'}]

你可以用index或者name来定位一个sheet，如果你没有传入sheet参数，则默认是第一个sheet。
你也可以输入这个sheet的title和除title外的数据行数：

For example:

    Data file is person.xls.

    Code:

        person = ReadXls('person.xls', 0)
        print person.title
        print 'nums of data is {0}.'.format(person.nums)

    Result:

        [u'id', u'name', u'mobile', u'address']
        nums of data is 3.


class:

ReadXls -- read xls and return a list (zipped first line and other rows)

    methods:

        __init__(book, sheet=0)
            open work_book and get specified sheet, which can be located by index or name. 0 DEFAULT.

        title
            return first line of sheet.

        data
            return zipped list.

        nums
            return line numbers of sheet(without first line). Case nums.

"""
from xlrd import open_workbook
from src.utils.config import DefaultConfig
from src.utils.utils_exception import DataFileNotAvailableException, DataError, SheetTypeError, SheetError
from src.utils.logger import Logger


class ExcelReader(object):
    def __init__(self, book, sheet=0):
        """Read workbook

        :param book: work_book name.Not path.
        :param sheet: index of sheet or sheet name.
        """
        self.logger = Logger(self.__class__.__name__).get_logger()
        self.book_name = '{0}\\{1}'.format(DefaultConfig().data_path, book)
        self.sheet_locator = sheet

        self.book = self._book()
        self.sheet = self._sheet()

    def _book(self):
        try:
            work_book = open_workbook(self.book_name)
        except IOError as e:
            raise DataFileNotAvailableException(e)
        self.logger.info('open workbook {0}'.format(self.book_name))
        return work_book

    def _sheet(self):
        """Return sheet"""
        if type(self.sheet_locator) not in [int, str]:
            raise SheetTypeError('Please pass in <type \'int\'> or <type \'str\'>, not {0}'.format(type(self.sheet)))
        elif type(self.sheet_locator) == int:
            try:
                sheet = self.book.sheet_by_index(self.sheet_locator)  # by index
            except:
                raise SheetError('Sheet \'{0}\' not exists.'.format(self.sheet_locator))
        else:
            try:
                sheet = self.book.sheet_by_name(self.sheet_locator)  # by name
            except:
                raise SheetError('Sheet \'{0}\' not exists.'.format(self.sheet_locator))
        self.logger.info('read sheet {0}'.format(self.sheet_locator))
        return sheet

    @property
    def title(self):
        """First row is title."""
        try:
            return self.sheet.row_values(0)
        except IndexError:
            raise DataError('This is a empty sheet, please check your file.')

    @property
    def data(self):
        """Return data in specified type:

            [{row1:row2},{row1:row3},{row1:row4}...]
        """
        sheet = self.sheet
        title = self.title
        data = list()

        # zip title and rows
        for col in range(1, sheet.nrows):
            s1 = sheet.row_values(col)
            s2 = [unicode(s).encode('utf-8') for s in s1]  # utf-8 encoding
            data.append(dict(zip(title, s2)))
        return data
    
#             for CaseExcel in CaseExcelList :
#             CaseDataList = GetCaseDataList(CaseExcel)
#             for CaseData in CaseDataList :
#                 Varstrlist = CaseData[3].split('\n')
#                 VarDict = {}
#                 #map(lambda x: VarDict.setdefault(x.split('=')[0],x.split('=')[1]), Varstrlist)
#                 for Varstr in Varstrlist:
#                     if '' != Varstr :
#                         try:
#                             l_index = Varstr.find('=')
#                             VarDict.setdefault(Varstr[0:l_index],Varstr[l_index+1:])
#                             #VarDict.setdefault(Varstr.split('=')[0],Varstr.split('=')[1])
#                         except:
#                             raise VariableError("TEST-DATA ERROR: %s" % CaseData[0])
#                 self.__DataDict[CaseData[0]] = (CaseData[1],CaseData[2],VarDict,CaseData[4])

    @property
    def nums(self):
        """Return the number of cases."""
        return len(self.data)


if __name__ == '__main__':
#     phone = ExcelReader('phone.xlsx', 0)
#     print phone.title
#     print phone.data
#     print phone.nums
#     row = phone.sheet.nrows
#     case_li = []
#     for i in range(row):
#         if i != 0:
#             case_li.append(phone.sheet.row_values(i))
#     print case_li
#     print len(case_li)

#     file_name = DefaultConfig().get('path', 'data')+"CP_WEB.ZCDL_JASON.xlsx" 
    file_name = "CP_WEB.ZCDL_JASON.xlsx" 
    print 'file_name---->',file_name
    phone = ExcelReader(file_name, 0)
    print phone.title
    print phone.data
    print phone.nums
    row = phone.sheet.nrows
    case_li = []
    for i in range(row):
        if i != 0:
            case_li.append(phone.sheet.row_values(i))
    print case_li
    print len(case_li)
    
    print 'kkk--->',phone.data[0][u'\u6d4b\u8bd5\u6570\u636e']