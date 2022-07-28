def blockAds(browser):
	all_iframes = browser.find_elements_by_tag_name("iframe")
	if len(all_iframes) > 0:
	    print("Ad Found\n")
	    browser.execute_script("""
	        var elems = document.getElementsByTagName("iframe"); 
	        for(var i = 0, max = elems.length; i < max; i++)
	             {
	                 elems[i].hidden=true;
	             }
	                          """)
