d={"Daniel":"Project","Charlie":"Prersentation","Jacob":"Presentation","James":"Presentation","Samantha":"Project"}
k=[]
for key in d:
    if d[key] != "Project":
        k.append(key)
        d[key]="washing"
print(k)
print(d)