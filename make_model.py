'''
coding:utf-8
@Software:PyCharm
@Time:2024/5/25 18:33
@Author:尘心||rocky
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# 加载预处理后的数据
df = pd.read_csv('preprocessed_eve_log.csv')
df = df.dropna()

# 特征和标签
X = df[['src_ip', 'src_port', 'dest_ip', 'dest_port', 'proto']]
y = df['alert']

# 将IP地址和协议转换为数值
X = pd.get_dummies(X, columns=['src_ip', 'dest_ip', 'proto'])

# 拆分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 特征标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 初始化随机森林分类器
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 训练模型
model.fit(X_train, y_train)

# 进行预测
y_pred = model.predict(X_test)

# 评估模型
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# 保存模型
joblib.dump(model, 'random_forest_model.pkl')
