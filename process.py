from pyspark import SparkContext, SparkConf, StreamingContext

conf = SparkConf().setAppName("Stand Alone Python Script")
sc = SparkContext(conf=conf)
ssc = new StreamingContext(sc,Seconds(1))
cc = CassandraConnector(sc.getConf)
x = sc.cassandraTable("PortfolioDemo","Stocks").collect()
print x
