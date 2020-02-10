FROM ubuntu:14.04

ADD sources.list /etc/apt/
ADD requirements.txt /root/requirements.txt
ADD ca.crt /usr/local/share/ca-certificates/ca.crt
ADD id_rsa     /root/.ssh/id_rsa
ADD id_rsa.pub /root/.ssh/id_rsa.pub
ADD id_rsa.pub /root/.ssh/authorized_keys
ADD startup.sh /startup.sh

RUN apt-get update && \
	sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d && \
	DEBIAN_FRONTEND=noninteractive \
	apt-get install -y --no-install-recommends lsof man-db mtr nmap openssh-server strace traceroute \
	bind9-host curl dnsutils ftp telnet tcpdump zlib1g-dev \
	python3-dev python3-pip python3-pyqt4 \
	python-cssselect python3-crypto python3-lxml python3-zmq && \
	pip3 install --upgrade setuptools pip && \
	pip install -r /root/requirements.txt -i https://pypi.douban.com/simple && \
	find /usr/lib/python2.7 -name '*.pyc' -delete && \
	echo 'UseDNS no' >> /etc/ssh/sshd_config && \
	echo 'UserKnownHostsFile /dev/null' >> /etc/ssh/ssh_config && \
	echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config && \
	sed -i /loginuid/s/^/#/ /etc/pam.d/sshd && \
	update-ca-certificates && \
	usermod -p '$6$sHTmsDVi$Spmhni61IjBGDsQBS/rYj1k4Do3u2HlI5qtCrPGn4mvqzogdagSjq0KqfeMXFpI2bqkg9OVOuZHEJOxtN.byy0' root && \
	useradd -d /home/brandon -G sudo -m -p '$6$sHTmsDVi$Spmhni61IjBGDsQBS/rYj1k4Do3u2HlI5qtCrPGn4mvqzogdagSjq0KqfeMXFpI2bqkg9OVOuZHEJOxtN.byy0' -s /bin/bash brandon && \
	sed -i /PermitRootLogin/s/without-password/yes/ /etc/ssh/sshd_config && \
	mkdir -p   /root/.ssh && \
	chmod -R og-rwx /root/.ssh && \
	sed -i '/sudo/s/ALL$/NOPASSWD: ALL/' /etc/sudoers && \
	update-locale && \
	rm -rf /var/lib/apt/lists/* /var/cache/* /var/log/* && \
	apt-get autoremove -y && apt-get clean -y

CMD ["/startup.sh"]
