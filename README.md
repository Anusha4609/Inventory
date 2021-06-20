# Inventory

1) Database Creation:
    a) Created Books model
    
2) Created services.py where the the google books API is integrated and the books from the api are fetched.

3) In the first page of application, displayed all the objects of books in a table.

   a) Provided details, edit and delete option on each of the row in the table.

   b) In **details**, the book of particular row is picked via id and we get the book details  

   c)In **edit** , the particular book details are loaded in the form and the changed made in quantity is saved to the Books table.

   d) In **delete**, the particular book is is fetched and that object is deleted.
   
4) In Add books:
  
   a) Input takes the name of the book from user and send that to the book api service function and the corresponding books are returned.
   
   b) The books are loaded in dropdown and upon selection by the user, we get the googlebook title, id and add to the out book table's name and id
   
   c) The quantity is taken from the user and is added to the book's quantity.
   
   d) Upon saving, all these details are added to the DB and we will redirect to the list page(first page)

