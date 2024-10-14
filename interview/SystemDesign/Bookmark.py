# Microsoft Suzhou Microsoft Edge Mobile Development team first round interview 
# system design for a chrome brower bookmark
# Design the table
# Design Bookmark and Folder, checking OOP

import datetime

class Database:
class BookmarkItem:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Bookmark(BookmarkItem):
    def __init__(self, id, url, create_time, name, folder_id):
        super().__init__(id, name)

        self.url = url
        self.create_time = create_time
        self.folder_id = folder_id


class Folder(BookmarkItem):
    def __init__(self, id, name, parent_id):
        super().__init__(id,name)
        self.parent_id = parent_id
        self.children = [] # list of Folders and Bookmarks
        # heap

    def add_children(self, item: BookmarkItem):
        self.children.append(item)

class BookmarkManger:
    def __init__(self) -> None:
        self.bookmarks = {}
        self.folders = {}
        self.nextID = 1
        self.root: Folder = Folder(0, "root")


    def create_bookmark(self, name, url, parent_id):
        bookmark = Bookmark(self.nextID, url, create_time=Date.now(), name)
        self.nextID += 1
        self.bookmarks[bookmark.id] = bookmark
        parent = self.folders.get(parent_id, self.root)
        parent.add_item(bookmark)

        return bookmark
    
    def create_folder(self,name, parent_id):
        folder = Folder(self.nextID, name)
        self.nextID += 1
        self.folders[folder.id] = folder

        parent = self.folders.get(parent_id)
        parent.add_item(folder)
        parent.add_children(folder)
        

        

    


    
# class BookmarkManager:
#     def __init__(self, database_name):
#         self.db = database_name
    
#     def add_bookmark(self, name, url, folder_id):
#         # create_time = date.now()
#         # # this is a adding query that insert into bookmark
#         # self.db.cursor.execute("")
#         # self.db.

#     def get_bookmark(self, id):
        
#         #self.db.cursor.execute("?")

