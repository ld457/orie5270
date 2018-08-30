from pyspark import SparkConf, SparkContext


def multi_matrix(a_txt, v_txt):

    conf = SparkConf()
    sc = SparkContext(conf=conf)

    data_a = sc.textFile(a_txt)
    data_v = sc.textFile(v_txt)

    a = data_a.map(lambda l: [float(i) for i in l.split(',')])
    v = data_v.map(lambda l: [float(i) for i in l.split(',')])
    a = a.zipWithIndex()
    a = a.map(lambda l: (l[1], [(col, item) for col, item in enumerate(l[0])]))
    v = v.zipWithIndex()
    v = v.map(lambda l: (l[1], l[0]))
    a = a.flatMapValues(lambda l: [i for i in l]).map(lambda l: (l[1][0], (l[0], l[1][1])))
    v = v.flatMapValues(lambda l: [i for i in l])

    av = a.join(v)
    av = av.map(lambda l: (l[1][0][0], l[1][0][1] * l[1][1]))
    av = av.reduceByKey(lambda n1, n2: n1 + n2)

    return av


if __name__ == '__main__':
    res = multi_matrix(a_txt='A.txt', v_txt='v.txt')
    print(res.collect())
