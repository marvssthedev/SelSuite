<h3>Prefered Selector Order</h3>
<ol>
    <li>ID</li>
    <li>NAME</li>
    <li>CSS_SELECTOR</li>
    <li>CLASS_NAME</li>
    <li>LINK_TEXT</li>
    <li>PARTIAL_LINK_TEXT</li>
    <li>TAG_NAME</li>
    <li>XPATH</li>
</ol>

<h3>Workflow</h3>
  Conftest      ->      test_*.py      <-      page.py      <--    base.py
                           ^
 ------------         ------------        ----------------        -----------------
 | Browser  |         | Browser  |        | page_methods |        | proto_methods |
 | URL      |         | User     |        ----------------        -----------------
 | User     |         | Password |       
 | Password |         ------------ 
 ------------

key:
->: sends
<-: recives
^: consumes
<--: inherits 
