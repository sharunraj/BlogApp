import webbrowser
website = input("Search Website: ")

if website == "amazon":
    amazon = input("search product: ")
    webbrowser.open("https://www.amazon.in/s?k=" + amazon)
elif website == "flipkart":
    flipkart = input("search product: ")
    webbrowser.open("https://www.flipkart.com/search?q="+flipkart)
