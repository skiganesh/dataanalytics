sudo apt-get update && apt-get dist-upgrade
sudo apt-get install openjdk-8-jdk
cd
cat <<EOT >> .bashrc
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
EOT
source .bashrc
sudo apt install openssh-server openssh-client -y
cat /dev/zero | ssh-keygen -q -N ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
cd /opt
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
tar -xzvf hadoop-3.3.0.tar.gz
ln -s hadoop-3.3.0 hadoop
cd
cat <<EOT >> .bashrc
# set up HADOOP_HOME
export HADOOP_HOME=/opt/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
EOT
source .bashrc
cd /opt/hadoop/etc/hadoop/
cat <<EOT >> hadoop-evn.sh
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop
EOT
cd /dataanalytics/HadoopInstallation
mv hdfs-site.xml /opt/hadoop/etc/hadoop/hdfs-site.xml
mv core-site.xml /opt/hadoop/etc/hadoop/core-site.xml
mv yarn-site.xml /opt/haoop/etc/hadoop/yarn-site.xml
mv mapred-site.xml /opt/haoop/etc/haoop/mapred-site.xml
hdfs namenode -format
cd /opt
wget https://downloads.apache.org/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz
tar -xzvf apache-hive-3.1.2-bin.tar.gz
ln -s apache-hive-3.1.2-bin hive
cd
cat <<EOT >> .bashrc
export HIVE_HOME=/opt/hive
export HIVE_CONF_DIR=/opt/hive
export PATH=$PATH:$HIVE_HOME/bin
EOT
source .bashrc
hdfs dfs -mkdir -p /user/hive/warehouse
hdfs dfs -chmod g+w /user/hive/warehouse
hdfs dfs -mkdir /tmp
hdfs dfs -chmod g+w /tmp
cd
mkdir mysqlconnector
cd mysqlconnector
sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java_8.0.23-1ubuntu16.04_all.deb

sudo dpkg -x mysql-connector-java_8.0.23-1ubuntu16.04_all.deb /
cd /usr/share/java
sudo cp mysql-connector-java-8.0.23.jar /usr/local/apache-hive-3.1.2-bin/lib
cd /usr/local/hadoop-3.3.0/share/hadoop/common/lib/
sudo cp  guava-27.0-jre.jar /usr/local/apache-hive-3.1.2-bin/lib/
cd /usr/local/apache-hive-3.1.2-bin/lib/
sudo mv guava-19.0.jar guava_back-19.0.jar
cd /opt/hive/conf
cp hive-default.xml.template hive-site.xml

