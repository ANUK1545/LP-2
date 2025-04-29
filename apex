File

Edit

Debug

Test

Workspace

Help

<

>

Code Coverage: None
63

Go To
1
public class BookHandler {
2
    
3
    // Method to insert a new Book record
4
    public static void insertBook(String bookName, String authorName, String publisherName) {
5
        try {
6
            // Create a new instance of Book__c
7
            Book__c newBook = new Book__c();
8
            newBook.Name = bookName;
9
            newBook.author_name__c = authorName;
10
            newBook.publisher__c = publisherName;
11
            
12
            // Insert the record
13
            insert newBook;
14
            
15
            System.debug('Book inserted successfully! Id: ' + newBook.Id);
16
        } catch (DmlException e) {
17
            System.debug('Error inserting Book: ' + e.getMessage());
18
        }
19
    }
20
}
21
 
 
Filter
Click here to filter the log list
