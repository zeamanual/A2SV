class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        duplicate_dic = {}

        for path in paths:
            path= path.split()
            files_count = len(path)-1

            root_path=path[0]+'/'

            for file_index in range(files_count):
                file_content,file_name=self.get_file_content(path[file_index+1])

                if(file_content in duplicate_dic):
                    duplicate_dic[file_content].append(root_path+file_name)
                else:
                    duplicate_dic[file_content] = [root_path+file_name]
        
        duplicates=[]
        for content in duplicate_dic.keys():
            if( len(duplicate_dic[content])>1):
                duplicates.append(duplicate_dic[content])

        return duplicates


    def get_file_content(self,file_data):
        
        file_content = ''
        file_name=''
        file_content_found=False
       
        for char in file_data:
            if(char =='('):
                file_content_found=True
                continue
            elif(char==')'):
                break

            if(file_content_found):
                file_content+=char
            else:
                file_name+=char
            
        return file_content,file_name
