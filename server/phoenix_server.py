#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import socket
from datetime import datetime
import server_ui
from colorama import Fore, Style
from PyQt6 import QtWidgets
from PyQt6.QtGui import QTextCursor


def current_date():
	date = str(datetime.now()).split('.')[0]

	return date


def msg(text: str, msg_type: str) -> str:
	"""Цветной и дружелюбный вывод сообщения

	Аргументы:
	 + text: str - текст сообщения
	 + print(msg_type: str - тип сообщения (info, warn, error)

	Вывод:
	 + str - цветное сообщение"""
	msg_type = msg_type.lower()

	if msg_type == 'info':
		return f'{Fore.GREEN}[INFO {current_date()}]{Style.RESET_ALL} {text}'
	elif msg_type == 'warn':
		return f'{Fore.YELLOW}[WARNING {current_date()}]{Style.RESET_ALL} {text}'
	elif msg_type == 'error':
		return f'{Fore.RED}[ERROR {current_date()}]{Style.RESET_ALL} {text}'
	else:
		return f'{Fore.CYAN}[{msg_type.upper()} {current_date()}]{Style.RESET_ALL} {text}'


class Server:
	def __init__(self, host: str, port: int):
		self.HOST = host
		self.PORT = port
		self.SERVER_ADDRESS = (self.HOST, self.PORT)

		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def bind(self) -> dict:
		"""Привязка сервера к адресу
		
		Возвращает при удачной привязке:
		 + dict {'status': True, 'info': ...}
		Возвращает при неудачной привязке:
		 + dict {'status': False, 'info': ...}"""
		try:
			self.server.bind(self.SERVER_ADDRESS)
			print(msg(f'Сервер успешно привязан к адресу {self.HOST}:{self.PORT}', 'info'))
		except Exception as ex:
			print(msg(f'Ошибка привязки сервера к адресу: {ex}', 'error'))
			
			return {'status': False,
					'info': f'Ошибка привязки сервера к адресу: {ex}'}
		else:
			return {'status': True,
					'info': f'Сервер успешно привязан к адресу {self.HOST}:{self.PORT}'}


class PhoenixServerUI(QtWidgets.QMainWindow, server_ui.Ui_MainWindow):
	def __init__(self):
		###### Инициализация и установка UI ######
		super().__init__()
		self.setupUi(self)

		###### UI элементы ######
		self.log_text.setEnabled(True)

		self.is_launched = False

		self.start_server_btn.clicked.connect(self.start_server)
		self.shutdown_btn.clicked.connect(self.shutdown_server)

	def shutdown_server(self):
		cursor = QTextCursor(self.log_text.document())
		self.log_text.setTextCursor(cursor)

		if self.is_launched:
			self.log_text.insertPlainText(f'\nСервер выключен')
			self.is_launched = False
		else:
			self.log_text.insertPlainText(f'\nСервер выключен')

	def start_server(self):
		cursor = QTextCursor(self.log_text.document())
		self.log_text.setTextCursor(cursor)

		if self.is_launched:
			self.log_text.insertPlainText(f'\nСервер уже запущен!')
		else:
			self.is_launched = True
			server_started_info = f'Сервер запущен на {self.ipaddr_line.text()}:{self.port_line.text()}'
			print(msg(server_started_info, 'info'))

			self.log_text.insertPlainText(f'\n{server_started_info}')


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = PhoenixServerUI()
	window.show()
	app.exec()


if __name__ == '__main__':
	main()
