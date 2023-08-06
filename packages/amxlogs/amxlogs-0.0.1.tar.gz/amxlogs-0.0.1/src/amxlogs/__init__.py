import asyncio
from logging import debug, info, warning, error


class LogSniffer():

	def __init__(self) -> None:
		pass


	def set_systems(self, systems):
		self.systems = systems
		info(f"LogSniffer added {len(self.systems)} systems")


	def config(self,
		user_name='administrator', password='password',
		log_type='error_log',
		path='',
		clear_logs=False,
		debug_ftp=0,
			):
		self.user_name = user_name
		self.password = password
		self.log = log_type
		if not path:
			path = f'systems/{self.log}/'
			self.path = path
		self.debug_ftp = debug_ftp
		self.clear_logs = clear_logs

		return


	async def _retrieve_logs(self, system):
		from os import mkdir
		import ftplib
		
		# connect ftp
		ftp = ftplib.FTP(
			system['master_ip'],
			user=self.user_name,
			passwd=self.password
			)
		ftp.debugging = self.debug_ftp

		# read top level directory
		try:
			files = ftp.nlst()  # not handling empty dir since we know there's something there
			if len(files) == 0:
				warning(f"files must be manually retrieved from {system['full_name']} (32MB NI-700) ftp://{system['master_ip']}")
		except Exception as e:
			error(f"amxlogs.py _retrieve_logs() {system['full_name']} {self.log} {e}")

		await asyncio.sleep(0)
		# filter
		try:
			for file in files:
				if (self.log == 'error_log' and file.lower().endswith('.log')) or file.endswith(f"{self.log}.txt") or file.endswith(f"{self.log.upper()}.TXT"):
					await asyncio.sleep(0)
					
					filename = f"{self.path}{system['full_name']} {file}"
					try:
						mkdir(f"{self.path}{[self.log]}")
					except FileExistsError:
						pass
					with open(filename, 'wb+') as f:
						ftp.retrbinary(f"RETR {file}", f.write)

					if self.clear_logs == 'True':
						ftp.delete(file)
			ftp.quit()
		except Exception as e:
			error(f"amxlogs.py _retrieve_logs() {self.log} for file in files: {e}")
			ftp.quit()
		return


	async def run(self):
		# filter down to systems with log files
		for system in self.systems:
			if self.log not in system: system[self.log] = False
		filtered_systems = [x for x in self.systems if x[self.log] is True]
		info(f"{self.log} found in {len(filtered_systems)} rooms:\n {[x['full_name'] for x in filtered_systems]}")

		tasks = []
		for i, _ in enumerate(filtered_systems):
			tasks.append(self._retrieve_logs(filtered_systems[i]))
		await asyncio.gather(*tasks)
		return
