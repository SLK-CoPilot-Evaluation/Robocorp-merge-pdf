''' Importing the required modules '''

import os
import PyPDF2


def merge_pdf(input_path, output_path):
    '''Defining the function'''
    try:
        
        # Storing the input path in the variable dirpath
        dirpath = input_path
        directory = os.listdir(dirpath)
        print(directory)
        # Declaring a list to store the files
        if len(directory) != 0:
            print(len(directory))
            files = []

            # Iterating through all the files in the directory and fetching all the pdf files
            for path in os.listdir(dirpath):
                if path.find(".") > -1:
                    if path[path.rindex(".")+1:len(path)].upper() == "PDF":
                        # Adding the pdf files to the list files
                        files.append(path)
                    else:
                        # Printing error message if the file is not in the supported format
                        print("File is not in the supported formats")
                        # raise Exception("File is not in the supported formats")
                else:
                    # Printing error message if there are no files with extensions
                    print("There are no files with the extensions")

            # Looping through each file in the list files
            pdf_writer = PyPDF2.PdfWriter()
            for file in files:
                # Reading the pdf file using PdfReader
                pdf_reader = PyPDF2.PdfFileReader(dirpath+"\\"+file)

                # Checking if the pdf is password protected
                if pdf_reader.isEncrypted is False:
                    # Looping through each page in the pdf
                    for page_num in range(pdf_reader.numPages):
                        # Getting the page object
                        page_obj = pdf_reader.getPage(page_num)
                        # Adding the page to the pdf writer
                        pdf_writer.addPage(page_obj)
                else:
                    # Printing error message if the pdf is password protected
                    raise Exception("PDf is password protected so it is rejected")

            # Writing the merged data to a new pdf file

            pdf_output_file = open(output_path, 'wb')
            pdf_writer.write(pdf_output_file)

        else:
            # Printing error message if there are no files in the directory
            print("No Files in the directory")

    except Exception as exception:
        # Printing the error message
        print(f"Error : {str(exception)}")
        raise exception
