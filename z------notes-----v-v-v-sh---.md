many notes in "commands.md" in instructor's computer ---- check screenshots --- IMPORTANT


<!-- time 10hr + -->

System check identified no issues (0 silenced).
September 25, 2024 - 17:02:31
Django version 5.1.1, using settings 'backend.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.


// ######     IMPORTANT NOTE      ######   
//       
python manage.py runserver 0.0.0.0:8000
http://192.168.43.167:8000/admin/login/?next=/admin/

// ######---------------------------//>>   

    final results = fetchProducts(context.watch<HomeTabNotifier>().queryType);
        context.read<HomeTabNotifier>().setRefetch(refetch); //sn=


  void setRefetch(Function() r) {   *************************************** ( 2 )
    ------------------------------------

  void setIndex(String index) {
    _index = index;

    switch (index) {
      case 'All':
        setQueryType(QueryType.all);
        refetch!();

        setQueryType(QueryType.all);



  void setQueryType(QueryType q) {
-------------------------------------------------------------------------------------');

<!-- fetch_products.dart -->
  Future<void> fetchData() async {

    useEffect(() {  **************************************************** ( 1 )
    fetchData();

  void refetch() { 
    fetchData();



 ---useEffect---D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrcproductshooksetch_products.dart----
 refetch set
 ---D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrchomecontrollershome_tab_notifier.dart---
 ----------------------------------------------
 refetch set
 ---D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrchomecontrollershome_tab_notifier.dart---
 ----------------------------------------------


<!-- ========        MEN        ======== -->
<!-- ========        MEN        ======== -->
<!-- ========        MEN        ======== -->
<!-- ========        MEN        ======== -->

<!-- ======================================================================== -->
    final results = fetchProducts(context.watch<HomeTabNotifier>().queryType); ^^^^^^^^ ( 2.5 )
        context.read<HomeTabNotifier>().setRefetch(refetch); //sn=

  void setRefetch(Function() r) {   *************************************** ( 2 )
                                    ^^^^^  refetch set ^^^^^^ ( 3 )
    ------------------------------------

  void setIndex(String index) {
    _index = index;

    switch (index) {
      case 'All':
        setQueryType(QueryType.all);                    ^^^^^^ ( 1 )
        refetch!();                 ^^^^^REFETCH RAN----^^^^^^ ( 2 ) 

        setQueryType(QueryType.all);


  void setQueryType(QueryType q) {  ^^^^^^^^^^^^^^^^^^^^^^^^ ( 1 )
-------------------------------------------------------------------------------------');

<!-- fetch_products.dart -->
  Future<void> fetchData() async {

    useEffect(() {  **************************************************** ( 1 )
    fetchData();


  void refetch() { 
    fetchData();

<!-- ======================================================================== -->

 ---men---------------D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrchomecontrollershome_tab_notifier.dart
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ( 1 )-------------------------------------------------------------
 
 REFETCH RAN----D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrcproductshooksetch_products.dart
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ( 2 ) ....... // already refetch set --- running here
 
 refetch set
 ---D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrchomecontrollershome_tab_notifier.dart---
 ----------------------------------------------
 
 ---men---------------D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrchomecontrollershome_tab_notifier.dart
 ----------------------------------------------------------------------------------------------------------------------------
 
 REFETCH RAN----D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrcproductshooksetch_products.dart
 refetch set
 ---D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrchomecontrollershome_tab_notifier.dart---
 ----------------------------------------------
 
 refetch set
 ---D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrchomecontrollershome_tab_notifier.dart---
 ----------------------------------------------
 
 refetch set
 ---D:src_devz--projecommerce-flutter-django-dbestech--ideosharinglibsrchomecontrollershome_tab_notifier.dart---
 ----------------------------------------------