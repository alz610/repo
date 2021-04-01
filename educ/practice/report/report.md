# Введение
## Слайд 1

Добрый день, расскажу про свою тему практики “Поддержка очереди задач IBM LSF в клиенте запуска расчетов на кластере Scheduler”


# Постановка задачи
## Слайд 2

Scheduler – это программа для планирования задач на кластере через графический пользовательский интерфейс (GUI)


## install.config

Plan your installation to determine the required parameters for the install.config file 
$ vi install.config

Choose a primary LSF administrator (owns the LSF and EGO configuration files and log files). For example, 
LSF_ADMINS="lsfadmin"

Choose a shared LSF installation directory. For example, 
LSF_TOP="/usr/share/lsf"

Choose LSF hosts (management host, management candidates, server hosts, and client-only hosts). For example, 
LSF_ADD_SERVERS="hostm hostb hostc hostd"
LSF_MASTER_LIST="hostm hostd"
LSF_ADD_CLIENTS="hoste hostf"

Choose LSF server hosts that are candidates to become the management host for the cluster, if you are installing a new host to be dynamically
added to the cluster. For example, LSF_MASTER_LIST="hosta hostb" 
Choose a cluster name that has 39 characters or less with no white spaces. For example, 
LSF_CLUSTER_NAME="cluster1"

If you are installing LSF Standard Edition, choose a configuration template to determine the initial configuration of your new cluster. For example, 
CONFIGURATION_TEMPLATE="HIGH_THROUGHPUT"
