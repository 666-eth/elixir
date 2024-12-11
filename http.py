#!/bin/bash

# 检查是否为 root 用户
if [ "$(id -u)" -ne 0 ]; then
  echo "请使用 root 用户运行此脚本！"
  exit 1
fi

# 定义变量
PORT=24121
USERNAME=qqq
PASSWORD=bgmailqqq

echo "开始安装 Squid..."

# 安装必要的工具
if [ -f /etc/redhat-release ]; then
  # CentOS 系统
  yum update -y
  yum install -y squid httpd-tools
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ]; then
  # Ubuntu/Debian 系统
  apt update -y
  apt install -y squid apache2-utils
else
  echo "未支持的系统！"
  exit 1
fi

# 创建用户名密码认证文件
htpasswd -bc /etc/squid/passwd $USERNAME $PASSWORD

# 配置 Squid
cat <<EOF > /etc/squid/squid.conf
http_port $PORT
auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic children 5
auth_param basic realm Squid Proxy
auth_param basic credentialsttl 2 hours
acl authenticated proxy_auth REQUIRED
http_access allow authenticated
http_access deny all
EOF

# 设置日志目录权限
chown -R proxy:proxy /var/log/squid

# 启动 Squid 并设置开机自启
systemctl enable squid
systemctl restart squid

# 输出结果
echo "Squid 安装完成！"
echo "HTTP 代理运行中："
systemctl status squid

