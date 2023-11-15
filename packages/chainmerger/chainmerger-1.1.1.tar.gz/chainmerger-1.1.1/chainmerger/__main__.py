from chainmerger.__version__ import __version__

import csv
from posixpath import splitext
import os, shutil
import pathlib
import argparse

import pandas
import tldextract
import openpyxl
import xlsxwriter

print('')
print('----- Chainalysis csv-export merging-tool ' + __version__ + ' -----')
print('')
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", dest="input", help="Input-path csv-export - else home/chainmerger_Input is used.")
parser.add_argument("-o", "--output", dest="output", help="Output-path csv-export - else home/chainmerger_Input/csvOutput is used.")
args = parser.parse_args()

# overwrite output
# copy last job's files in new folder

#####
##### Configurations
#####

ex_y = 4    # row in which the transaction-receiving exchange is found
ex_x = 0    # element in row, which specifies the exchange
max_col = 9 # amount of columns to add each row (so each row has the same - needed for converting to xlsx) 
cut_ar1 = [1,2,3,6,7,8,27] # cut first
cut_ar2 = [1,2,3,6,7,8,27] # cut following files
cut_ar2.extend(range(11,25,1))
report = "chainalysis_report.xlsx"

#####
##### Variables
#####

inputpath = ""
outputpath = ""
reportfile = ""
mergedcsv = ""
mergedxlsx = ""

#####
##### Argument handling
#####

# if input/output, then used, else check home and add input/output dir
def preparedirs():
    global inputpath
    global outputpath
    global reportfile
    global mergedcsv
    global mergedxlsx
    if args.input: # if input given, create folder; else create default in home
        try:
            inputpath = args.input 
            if not os.path.exists(inputpath):
                os.mkdir(inputpath)
                print('Inputpath: ' + args.input)
        except Exception as e:
            print("Couldn't create path %s. Reason: %s" % (args.input,e))
            exit()
    else:
        inputpath = os.path.join(pathlib.Path.home(), "chainmerger_Input")
        if not os.path.exists(os.path.join(pathlib.Path.home(), "chainmerger_Input")): 
            os.mkdir(os.path.join(pathlib.Path.home(), "chainmerger_Input"))
            print('Input-path not specified. Adding for you at' + inputpath)
            print('Add chainalysis exported CSV files and press Enter to continue...')
            input()
        else:
            print('Inputpath: ' + inputpath)
        while not any(os.scandir(inputpath)):
            print('Missing input-files at ' + inputpath)
            print('Add chainalysis exported CSV files and press Enter to continue...')
            input() 
    if args.output: # if output given, create folder; else create default in home
        try:
            outputpath = args.output
            if not os.path.exists(outputpath):
                os.mkdir(outputpath)
                print('Outputpath: ' + args.output)
        except Exception as e:
            print("Couldn't create path %s. Reason: %s" % (args.output,e))
            exit()
    else:
        outputpath = os.path.join(inputpath, "chainmerger_Output")
        if not os.path.exists(os.path.join(inputpath, "chainmerger_Output")): 
            os.mkdir(os.path.join(inputpath, "chainmerger_Output"))
            print('Output-path not specified. Adding for you at' + outputpath)
            print('')
        else:
            print('Outputpath: ' + outputpath)

    # copy all inputs to outputdir
    x = 1
    for i in read_csv_dir(inputpath):
        shutil.copy(i, os.path.join(outputpath, os.path.basename(i)))
        print('--> ' + os.path.basename(i))
        x += 1
    print('Found ' + str(x) + ' files for input.')
    print('')

    if not os.path.exists(os.path.join(outputpath, 'csv')): os.mkdir(os.path.join(outputpath, 'csv'))
    mergedcsv = os.path.join(outputpath, 'csv')
    if not os.path.exists(os.path.join(outputpath, 'xlsx')): os.mkdir(os.path.join(outputpath, 'xlsx'))
    mergedxlsx = os.path.join(outputpath, 'xlsx')

    # add report-file to output
    reportfile = os.path.join(outputpath, report)
    open(reportfile, 'a').close

def clean_output():
    print('Cleaning up output...')
    print('')
    if os.path.exists(outputpath): # remove the content of output-directory for the new job
            for file in os.listdir(outputpath):
                filepath = os.path.join(outputpath, file)
                if report in file:
                    continue
                try:
                    if os.path.isfile(filepath) or os.path.islink(filepath):
                        os.remove(filepath)
                    if os.path.isdir(filepath):
                        shutil.rmtree(filepath)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (filepath,e))
                    exit()

#####
##### do the work
#####

def read_csv_dir(dir): # give it a dir and it puts all csv-content in array (with path), leaving non-csv untouched
    array = []
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            if file.endswith('.csv'):
                array.append(os.path.join(dir, file))
    return(array)

def csv_exchange_extractor(file, row_nr, row_ele): # gives back the specified row element of file x to caller
    reader = csv.reader(open(file,'r'), delimiter=',')
    rows = list(reader)
    return(tldextract.extract(rows[row_nr][row_ele])[1]) #tldextract removes toplevel-domain from Exchange (.com etc.)

# creates folder for each existing Exchange, extracted by the csv files inside specified folder
# puts all these files in the according Exchange-dirs
# finally renames them to <int><Exchange>.csv incrementally
def sort2Exchange(): 
    exchange_array = []
    for i in read_csv_dir(outputpath):
        exchange = csv_exchange_extractor(i, ex_y, ex_x)
        if not exchange in exchange_array:
            exchange_array.append(exchange)
        if not os.path.exists(os.path.join(outputpath, exchange)):
            os.mkdir(os.path.join(outputpath, exchange))
        shutil.move(i, os.path.join(outputpath, csv_exchange_extractor(i, ex_y, ex_x)))
    for folder in os.listdir(outputpath):
        dataset_count = 1
        if os.path.isdir(os.path.join(outputpath, folder)):
            for csvfile in read_csv_dir(os.path.join(outputpath, folder)):
                    newname = str(dataset_count) + csv_exchange_extractor(csvfile,ex_y,ex_x) + '.csv'  #Tuple: line 4 element 0 = Exchange
                    os.rename(csvfile, os.path.join(os.path.join(os.path.join(outputpath, folder), newname)))
                    dataset_count += 1
      
# iterates through each exchange folder
# iterates through each file in them
# cuts all lines, specified in array1 & 2, writes into 1 file
def cutter(): 
    print('Merging datasets to file per Exchange:')
    for folder in os.listdir(outputpath):
        if folder == 'csv' or folder == 'xlsx': continue # skip the folders with the merged files
        else:
            if os.path.isdir(os.path.join(outputpath, folder)):
                file_list = os.listdir(os.path.join(outputpath, folder)) # create list of csv files and sort by number
                file_list = sorted(file_list, key=lambda x: x[:1])
                with open(os.path.join(mergedcsv, folder + '.csv'), 'a') as outfile:
                    dataset_count = 0
                    header = True # control if description headers will be kept or deleted (usually keep only in first dataset)
                    for i in file_list:
                        dataset_count+=1 # counts amount of files (sets), merged in file
                        csvfile = os.path.join(outputpath, folder, str(i))
                        with open(csvfile, newline='') as infile:
                            writer = csv.writer(outfile)
                            reader = csv.reader(infile)
                            row_nr=1
                            for row in reader:
                                while len(row) < max_col: row.append(None) # add columns until each row has the same
                                # if first file array1
                                if header == True:
                                    if not row_nr in cut_ar1:
                                        writer.writerow(row)
                                    row_nr+=1
                                # if other then array2
                                if header == False:
                                    if not row_nr in cut_ar2:
                                        writer.writerow(row)
                                    row_nr+=1
                            writer.writerow([None])
                            for i in [1,2]: # add 2 lines of hash between data-sets
                                hashline = ""
                                for i in range(1,200,1):
                                    hashline+='#'
                                writer.writerow([str(hashline)])
                            writer.writerow([None])
                        header = False
                    print('--> ' + str(dataset_count) + ' ' + str(folder))
    print('')


                
def merger(): # merges given csv files into 1 xlsx
    print('Adding merged sets to report:')
    for i in read_csv_dir(mergedcsv):
        infile = i
        outfile = os.path.join(mergedxlsx, splitext(os.path.basename(i))[0] + '.xlsx')
        pandas.read_csv(infile, delimiter=',', header=None).to_excel(outfile, index=False)
    writer = pandas.ExcelWriter(reportfile, engine='xlsxwriter')
    for i in os.listdir(mergedxlsx):
        df_list = []
        df = pandas.DataFrame(pandas.read_excel(os.path.join(mergedxlsx, i)))
        df.to_excel(writer, sheet_name=splitext(i)[0], index=None, header=None)
        print('--> added sheet ' + splitext(i)[0])
    writer.close()
    print('-----> ' + reportfile)
    print('')

def set_column_widths(): # sets column widths in xlsx reportfile using openpyxl
    print('Setting column widths to autosize content:')
    # open reportfile
    wb = openpyxl.load_workbook(reportfile)
    # iterate through sheets
    for sheet in wb:
        print('-----> resized sheet ' + sheet.title)
        # iterate through columns until max_col is reached
        for col in sheet.iter_cols(min_col=2, max_col=max_col+1):
            # get minimum column width for content of each column
            col_width = 0
            for cell in col:
                if cell.value:
                    if len(str(cell.value)) > col_width:
                        col_width = len(str(cell.value)) + 2 # add 2 to width to avoid cutting off last character
            sheet.column_dimensions[col[0].column_letter].width = col_width
    wb.save(reportfile)
    print('')

#####
##### MAIN
#####

def main():
    preparedirs()
    sort2Exchange()
    cutter()
    merger()
    set_column_widths()
    clean_output()
    print('----- Work done. Report ready -----')
    print('')


if __name__ == "__main__":
    main()
