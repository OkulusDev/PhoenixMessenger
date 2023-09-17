#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""phoenix_server.py - серверная часть
Phoenix Messenger - Быстрый, простой, анонимный и защищенный мессенджер
Copyright (c) 2023 Okulus Dev
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import sys
import socket
from threading import Thread
from colorama import init, Fore, Style
import rsa


def msg(text: str, msg_type: str) -> str:
	"""Цветной и дружелюбный вывод сообщения

	Аргументы:
	 + text: str - текст сообщения
	 + print(msg_type: str - тип сообщения (info, warn, error)

	Вывод:
	 + str - цветное сообщение"""
	msg_type = msg_type.lower()

	if msg_type == 'info':
		return f'{Fore.GREEN}[INFO]{Style.RESET_ALL} {text}'
	elif msg_type == 'warn':
		return f'{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {text}'
	elif msg_type == 'error':
		return f'{Fore.RED}[ERROR]{Style.RESET_ALL} {text}'
	else:
		return f'{Fore.CYAN}[{msg_type.upper()}]{Style.RESET_ALL} {text}'


class PhoenixServer:
	"""Сервер Phoenix"""
	def __init__(self, host: str, port: int):
		"""Инициализация сервера Phoenix Messenger

		Аргументы:
		 + host: str - хост, IP-адрес сервера
		 + port: int - порт сервера"""
		# Создание констант адреса сервера
		print(msg('Инициализация сервера...', 'info'))
		self.HOST = host
		self.PORT = port
		self.SERVER_ADDRESS = (self.HOST, self.PORT)

		# Создание сокета сервера
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def bind(self) -> bool:
		"""Связывание сокета сервера с адресом"""
		try:
			self.server.bind(self.SERVER_ADDRESS)
			print(msg(f'Сервер запущен на {self.HOST}:{self.PORT}', 'info'))
		except Exception as ex:
			print(msg(f'Ошибка связывание сервера: {ex}', 'error'))
			return False
		else:
			return True

	def listen(self):
		print(msg('Ждем подключений...', 'info'))

		try:
			self.server.listen()
			
			while True:
				client, addr = self.server.accept()
				print(msg(f'Клиент {addr} подключился', 'info'))
		except KeyboardInterrupt:
			print(msg('Сервер преврал свою работу по причине клавиатурного прерывания', 'WARN'))
			self.shutdown()

	def shutdown(self):
		print(msg('Выключение сервера...', 'warn'))
		self.server.close()
		sys.exit()

	def run(self):
		if self.bind():
			self.listen()
		else:
			self.shutdown()


def main():
	init(autoreset=True)
	phoenix_server = PhoenixServer('127.0.0.1', 8080)
	phoenix_server.run()


if __name__ == '__main__':
	main()
