
import baseLoader
import csvToXlsx
import finish
import parse
import chooseApp
import prepare

prepare.prepare()
baseLoader.requrl()
parse.parse()
csvToXlsx.csvtoexcel()
chooseApp.chooseapp()
finish.finish()