# -*- coding: utf-8 -*-
import os,re,string
import xlrd
from robot.errors import DataError, VariableError

TestCasePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + "/testcase"



def GetCaseDataList(caseExcel):
    """
    @name    :  GetCaseDataList
    @brief   :  Get test data list
    @parem   :  <caseExcel>
                <caseExcel> : File absolute path of case-excel

    @return  :  DataList :[['CaseNo','CaseLevel','CasePlat','CaseVar'],,,]
    @pkgpath :
    @remark  :
    @author  :  Jarvis
    @history :  Create 2015/8/20
    """
    filetag = os.path.splitext(caseExcel)[1][1:]
    if filetag != 'xlsx' and filetag != 'xls' :
        print "ERROR:the file '%s' is not Excel" % caseExcel
        assert 1==0

    AuotCaseDataList = []

    rb=xlrd.open_workbook(caseExcel,'r')
    sheetObjList = rb.sheets()
    for i in range(len(sheetObjList)):
        nrows = sheetObjList[i].nrows
        ncols = sheetObjList[i].ncols

        CaseNo    = -1
        CaseLevel = -1
        CaseVar   = -1
        CasePlat  = -1
        CaseAuto  = -1
        CaseName  = -1

        for j in range(ncols):
            colname = sheetObjList[i].row(0)[j].value
            if u'用例编号' == colname :
                CaseNo = j
            elif u'用例级别' == colname :
                CaseLevel = j
            elif u'测试数据' == colname :
                CaseVar = j
            elif u'测试环境' == colname :
                CasePlat = j
            elif u'自动化支持' == colname :
                CaseAuto = j
            elif u'用例名称' == colname :
                CaseName = j
            else:
                pass

        if CaseNo < 0 or CaseLevel < 0 or CaseVar < 0 or CasePlat < 0 or CaseAuto < 0 :
            print "ERROR:The excel '%s' is not test case Excel" % caseExcel
            assert 1==0

        for j in range(nrows):
            if 0 == j :
                continue

            AutoTag = sheetObjList[i].col(CaseAuto)[j].value
            if u'是' != AutoTag and 'Y' != AutoTag :
                continue

            AuotCaseData = []
            AuotCaseData.append(sheetObjList[i].col(CaseNo)[j].value)
            AuotCaseData.append(sheetObjList[i].col(CaseLevel)[j].value)
            AuotCaseData.append(sheetObjList[i].col(CasePlat)[j].value)
            AuotCaseData.append(sheetObjList[i].col(CaseVar)[j].value)
            AuotCaseData.append(sheetObjList[i].col(CaseName)[j].value)
            AuotCaseDataList.append(AuotCaseData)
    return AuotCaseDataList



class testCaseData():
    """
    @name    :  testCaseData
    @brief   :  Test case data dict
    @pkgpath :
    @remark  :
    @author  :  Jarvis
    @history :  Create 2015/8/20
    """
    __DataDict = {}

    def __init__(self,path):
        '''
        @name    :  __init__
        @parem   :  path : Directory of case-excel
        '''
        CaseExcelList = GetFileList('xlsx',path) + GetFileList('xls',path)
        for CaseExcel in CaseExcelList :
            CaseDataList = GetCaseDataList(CaseExcel)
            for CaseData in CaseDataList :
                Varstrlist = CaseData[3].split('\n')
                VarDict = {}
                #map(lambda x: VarDict.setdefault(x.split('=')[0],x.split('=')[1]), Varstrlist)
                for Varstr in Varstrlist:
                    if '' != Varstr :
                        try:
                            l_index = Varstr.find('=')
                            VarDict.setdefault(Varstr[0:l_index],Varstr[l_index+1:])
                            #VarDict.setdefault(Varstr.split('=')[0],Varstr.split('=')[1])
                        except:
                            raise VariableError("TEST-DATA ERROR: %s" % CaseData[0])
                self.__DataDict[CaseData[0]] = (CaseData[1],CaseData[2],VarDict,CaseData[4])
        pass

    def GetVariable(self,CaseNo,VarName):
        """
        @name    :  GetVariable
        @brief   :  Get variable value
        @parem   :  <CaseNo><VarName>
                    <CaseNo> : Test case No
                    <VarName>: Variable name
        @return  :  Variable value
        @pkgpath :
        @remark  :
        @author  :  Jarvis
        @history :  Create 2015/8/20
        """
        value = self.__DataDict[CaseNo][2][VarName]
        return value


    def GetScriptName(self):
        """
        @name    :  GetScriptName
        @brief   :  Get script name
        @parem   :  <Level><Plat>
                    <Level> : Test case No
                    <Plat>: Variable name
        @return  :  ScriptName list
        @pkgpath :
        @remark  :
        @author  :  Jarvis
        @history :  Create 2015/8/25
        """
        Level = 'ALL'
        Plat = 'ALL'
        ConfigFile = TestCasePath+'/config.ini'
        if os.path.isfile(ConfigFile) == True :
            fileHand = open(ConfigFile,'r')
            lineList = fileHand.readlines()
            fileHand.close()
            for line in lineList:
                strlist = line[:-1].split('=')
                if strlist[0] == 'LEVEL':
                    Level = strlist[1].strip()
                if strlist[0] == 'PLAT':
                    Plat = strlist[1].strip()

        ScriptNameList = []
        for key in self.__DataDict.keys() :
            if 'ALL' != Plat and self.__DataDict[key][1] != Plat:
                continue
            if 'ALL' != Level:
                ilevel1 = string.atoi(Level[-1:])
                ilevel2 = string.atoi(self.__DataDict[key][0][-1:])
                if ilevel1 < ilevel2:
                    continue
            ScriptNameList.append(key+'-'+self.__DataDict[key][3])
        return ScriptNameList




def GetCaseDataListB(caseExcel):
    """
    @name    :  GetCaseDataList
    @brief   :  Get test data list
    @parem   :  <caseExcel>
                <caseExcel> : File absolute path of case-excel

    @return  :  DataList :[['CaseNo','CaseLevel','CasePlat','CaseVar'],,,]
    @pkgpath :
    @remark  :
    @author  :  Jarvis
    @history :  Create 2015/8/20
    """
    filetag = os.path.splitext(caseExcel)[1][1:]
    # print "ok8888888  %s "  %(os.path.splitext(caseExcel)[0].split("/")[-1])
    if filetag != 'xlsx' and filetag != 'xls':
        print "ERROR:the file '%s' is not Excel" % caseExcel
        assert 1 == 0

    # 判断路径是否存在，不存在，创建路径：E:\\script\\xls_name
    # xls_name=os.path.splitext(caseExcel)[0].split("/")[-1]
    # FILE_PATH = "E:/script/"+os.path.splitext(caseExcel)[0].split("/")[-1]
    # if not os.path.exists(FILE_PATH):
    #     os.makedirs(FILE_PATH)

    AuotCaseDataList = []

    rb = xlrd.open_workbook(caseExcel, 'r')
    sheet_names = rb.sheet_names()
    # print sheet_names
    sheetObjList = rb.sheets()


    for i in range(len(sheetObjList)):

        __DataDict = {}
        # AuotCaseData = []

        sheet_name = sheet_names[i]
        # print "sheet_name is %s"  %(sheet_name)
        # file_abs = FILE_PATH+"/"+sheet_name+".txt"
        # myfile = open(file_abs, "w")
        # myfile.write(aaa+'\n')


        nrows = sheetObjList[i].nrows
        ncols = sheetObjList[i].ncols
        #print "ncols is %s " %(ncols)

        iGameId = -1
        methodid = -1
        sOpenNum = -1
        codes = -1
        nums = -1
        BonusResult = -1
        iWinCount = -1
        iWinCount1 = -1
        iWinCount2 = -1
        iWinCount3 = -1
        iWinCount4 = -1
        iWinCount5 = -1
        sPosition = -1

        for j in range(ncols):
            colname = sheetObjList[i].row(0)[j].value
            if 'CaseNo' == colname:
                CaseNo = j
            elif 'CaseName' == colname:
                CaseName = j
            elif 'iGameId' == colname:
                iGameId = j
            elif 'methodid' == colname:
                methodid = j
            elif 'iType' == colname:
                iType = j
            elif 'sOpenNum' == colname:
                sOpenNum = j
            elif 'codes' == colname:
                codes = j
            elif 'nums' == colname:
                nums = j
            elif 'BonusResult' == colname:
                BonusResult = j
            elif 'iWinCount' == colname:
                iWinCount = j
            elif 'iWinCount1' == colname:
                iWinCount1 = j
            elif 'iWinCount2' == colname:
                iWinCount2 = j
            elif 'iWinCount3' == colname:
                iWinCount3 = j
            elif 'iWinCount4' == colname:
                iWinCount4 = j
            elif 'iWinCount5' == colname:
                iWinCount5 = j
            elif 'sPosition' == colname:
                sPosition = j
            else:
                pass

        if iGameId < 0 or methodid < 0 or sOpenNum < 0 or codes < 0 or BonusResult < 0 :
            print "ERROR:The excel '%s' is not test case Excel" % caseExcel
            assert 1 == 0

        for j in range(nrows):
            if 0 == j:
                continue

            # AutoTag = sheetObjList[i].col(CaseAuto)[j].value
            # if u'是' != AutoTag and 'Y' != AutoTag :
            #     continue

            AuotCaseData = []
            AuotCaseData.append(sheetObjList[i].col(CaseNo)[j].value)
            AuotCaseData.append(sheetObjList[i].col(CaseName)[j].value)
            AuotCaseData.append(sheetObjList[i].col(iGameId)[j].value)
            AuotCaseData.append(sheetObjList[i].col(methodid)[j].value)
            AuotCaseData.append(sheetObjList[i].col(iType)[j].value)
            if sPosition >=0:
                AuotCaseData.append(sheetObjList[i].col(sPosition)[j].value)
            AuotCaseData.append(sheetObjList[i].col(sOpenNum)[j].value)
            AuotCaseData.append(sheetObjList[i].col(codes)[j].value)
            if nums > 0:
                AuotCaseData.append(sheetObjList[i].col(nums)[j].value)
            AuotCaseData.append(sheetObjList[i].col(BonusResult)[j].value)
            if iWinCount > 0:
                AuotCaseData.append(sheetObjList[i].col(iWinCount)[j].value)
            if iWinCount1 >=0:
                AuotCaseData.append(sheetObjList[i].col(iWinCount1)[j].value)
            if iWinCount2 >=0:
                AuotCaseData.append(sheetObjList[i].col(iWinCount2)[j].value)
            if iWinCount3 >=0:
                AuotCaseData.append(sheetObjList[i].col(iWinCount3)[j].value)
            if iWinCount4 >=0:
                AuotCaseData.append(sheetObjList[i].col(iWinCount4)[j].value)
            if iWinCount5 >=0:
                AuotCaseData.append(sheetObjList[i].col(iWinCount5)[j].value)
            AuotCaseDataList.append(AuotCaseData)
        #print AuotCaseDataList
    return AuotCaseDataList



class testCaseDataB():
    """
    @name    :  testCaseData
    @brief   :  Test case data dict
    @pkgpath :
    @remark  :
    @author  :  Jarvis
    @history :  Create 2015/8/20
    """
    __DataDict = {}

    def __init__(self,path):
        '''
        @name    :  __init__
        @parem   :  path : Directory of case-excel
        '''
        CaseExcelList = GetFileList('xlsx',path) + GetFileList('xls',path)
        for CaseExcel in CaseExcelList :
            CaseDataList = GetCaseDataListB(CaseExcel)
            for CaseData in CaseDataList :
                # Varstrlist = CaseData[3].split('\n')
                # VarDict = {}
                # #map(lambda x: VarDict.setdefault(x.split('=')[0],x.split('=')[1]), Varstrlist)
                # for Varstr in Varstrlist:
                #     if '' != Varstr :
                #         try:
                #             l_index = Varstr.find('=')
                #             VarDict.setdefault(Varstr[0:l_index],Varstr[l_index+1:])
                #             #VarDict.setdefault(Varstr.split('=')[0],Varstr.split('=')[1])
                #         except:
                #             raise VariableError("TEST-DATA ERROR: %s" % CaseData[0])
                self.__DataDict[CaseData[0]] = (CaseData)
        #print len(self.__DataDict)
        #print type(self.__DataDict["AHK3_3XZXDS_006"])
        #print (self.__DataDict["AHK3_3XZXDS_006"][0])
        pass

    def GetVariable(self,CaseNo,VarName):
        """
        @name    :  GetVariable
        @brief   :  Get variable value
        @parem   :  <CaseNo><VarName>
                    <CaseNo> : Test case No
                    <VarName>: Variable name
        @return  :  Variable value
        @pkgpath :
        @remark  :
        @author  :  Jarvis
        @history :  Create 2015/8/20
        """
        value = self.__DataDict[CaseNo][2][VarName]
        return value


    def GetScriptName(self):
        """
        @name    :  GetScriptName
        @brief   :  Get script name
        @parem   :  <Level><Plat>
                    <Level> : Test case No
                    <Plat>: Variable name
        @return  :  ScriptName list
        @pkgpath :
        @remark  :
        @author  :  Jarvis
        @history :  Create 2015/8/25
        """
        Level = 'ALL'
        Plat = 'ALL'
        ConfigFile = TestCasePath+'/config.ini'
        if os.path.isfile(ConfigFile) == True :
            fileHand = open(ConfigFile,'r')
            lineList = fileHand.readlines()
            fileHand.close()
            for line in lineList:
                strlist = line[:-1].split('=')
                if strlist[0] == 'LEVEL':
                    Level = strlist[1].strip()
                if strlist[0] == 'PLAT':
                    Plat = strlist[1].strip()

        ScriptNameList = []
        for key in self.__DataDict.keys() :
            if 'ALL' != Plat and self.__DataDict[key][1] != Plat:
                continue
            if 'ALL' != Level:
                ilevel1 = string.atoi(Level[-1:])
                ilevel2 = string.atoi(self.__DataDict[key][0][-1:])
                if ilevel1 < ilevel2:
                    continue
            ScriptNameList.append(key+'-'+self.__DataDict[key][1])
        #print "key---->%s,__DataDict---->>>>>%s " % (key, self.__DataDict[key][1])
        return ScriptNameList

    def GetDictList(self,CaseNo):
        """
        @name    :  GetVariable
        @brief   :  Get variable value
        @parem   :  <CaseNo><VarName>
                    <CaseNo> : Test case No
                    <VarName>: Variable name
        @return  :  Variable value
        @pkgpath :
        @remark  :
        @author  :  Jarvis
        @history :  Create 2015/8/20
        """
        #print CaseNo,self.__DataDict
        value2 = self.__DataDict[CaseNo]
        return value2



def GetCaseDataObj():
    """
    @name    :  GetCaseDataObj
    @brief   :  Get test data object
    @parem   :  NULL
    @return  :  Object of testCaseData
    @pkgpath :
    @remark  :
    @author  :  Jarvis
    @history :  Create 2015/8/21
    """
    ConfigFile = TestCasePath + '/config.ini'
    if os.path.isfile(ConfigFile) == True:
        fileHand = open(ConfigFile, 'r')
        lineList = fileHand.readlines()
        fileHand.close()
        for line in lineList:
            strlist = line[:-1].split('=')
            if strlist[0] == 'FLAGA':
                FLAGA = strlist[1].strip()
            if strlist[0] == 'FLAGB':
                FLAGB = strlist[1].strip()
    if FLAGA != None:
        #print FLAGA
        TestCasePathA = TestCasePath + "/" + FLAGA + "/"
        __CaseDataObj__ = testCaseData(TestCasePathA)
    return __CaseDataObj__


def GetCaseDataObjB():
    """
    @name    :  GetCaseDataObj
    @brief   :  Get test data object
    @parem   :  NULL
    @return  :  Object of testCaseData
    @pkgpath :
    @remark  :
    @author  :  Jarvis
    @history :  Create 2015/8/21
    """
    ConfigFile = TestCasePath + '/config.ini'
    if os.path.isfile(ConfigFile) == True:
        fileHand = open(ConfigFile, 'r')
        lineList = fileHand.readlines()
        fileHand.close()
        for line in lineList:
            strlist = line[:-1].split('=')
            if strlist[0] == 'FLAGA':
                FLAGA = strlist[1].strip()
            if strlist[0] == 'FLAGB':
                FLAGB = strlist[1].strip()
    if FLAGB != None:
        TestCasePathB = TestCasePath + "/" + FLAGB + "/"
        __CaseDataObj__ = testCaseDataB(TestCasePathB)

    return __CaseDataObj__




def GetFileList(tag,path):
    """
    @name    :  GetFileList
    @brief   :  Get file<tag> list
    @parem   :  <tag><path>
                <tag> : File extension
                <path>: File Directory
    @return  :  FileList
    @pkgpath :
    @remark  :
    @author  :  Jarvis
    @history :  Create 2015/8/20
    """
    FileList = []
    if re.match(".*\$RECYCLE\.BIN$",path) != None or re.match(".*System Volume Information$",path) != None:
        return FileList

    if os.path.isdir(path) == True :
        if path[-1:] != '/' and path[-1:] != '\\' :
            path = path + '/'
        PathList = os.listdir(path)
        for file in PathList:
            FileList = FileList + GetFileList(tag,path+file)
    else :
        if os.path.isfile(path) == True :
            if os.path.splitext(path)[1][1:] == tag and  ( '~' not in os.path.splitext(path)[0]):
                FileList.append(path)
    return FileList

