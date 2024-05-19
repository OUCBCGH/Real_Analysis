import itertools as its
#list(its.product([0,2],repeat=3))
def data_get(N):#N大于等于1
    for delta in range(2):
        for Tuple in its.product([0,2],repeat=N):
            yield (delta/3^N+sum([Tuple[i]/3^(i+1) for i in range(N)]),delta/2^N+sum([Tuple[i]*0.5/2^(i+1) for i in range(N)]))

def line_get(N):#N大于等于1
    for Tuple in its.product([0,2],repeat=N-1):
        yield [(2/3^N+sum([Tuple[i]/3^(i+1) for i in range(N-1)]),1/2^N+sum([Tuple[i]*0.5/2^(i+1) for i in range(N-1)])),(1/3^N+sum([Tuple[i]/3^(i+1) for i in range(N-1)]),1/2^N+sum([Tuple[i]*0.5/2^(i+1) for i in range(N-1)]))]

p1=arrow2d((0,0), (1.25,0), color='black' ,width=0.5, arrowsize=1)
p2=arrow2d((0,0), (0,1.25), color='black' ,width=0.5, arrowsize=1)
p3=list_plot(list(data_get(5)), pointsize=1)
#p4=line(list(line_get(5)),thickness=0.5)
p4=line([])
for i in range(1,6):
    for a in line_get(i):
        p4=p4+line(a,thickness=0.5)
show(p1+p2+p3+p4,axes=False,aspect_ratio=1, typeset='latex')