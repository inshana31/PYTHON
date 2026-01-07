blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
trafic=1000
for i in (blog_views):
    if blog_views >trafic:
        print("High Traffic")
    elif 500 <= blog_views <= 1000:
        print("Average")
    else:
        print("Low Traffic")
        
total=sum(blog_views)
print(total)


    