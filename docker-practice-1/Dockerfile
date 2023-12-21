FROM node
	LABEL maintainer ian.miell@gmail.com
	RUN git clone -q https://github.com/HazelDaniel/docker-practice.git
	WORKDIR ./todo
	RUN npm install > /dev/null
	EXPOSE 8000
	CMD ["npm", "start"]
