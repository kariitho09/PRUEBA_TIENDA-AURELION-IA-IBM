# tests.py: Tests mínimos para el router de opciones.

import unittest
from unittest.mock import patch, MagicMock
import asyncio
from main import procesar_opcion

class TestRouterOpciones(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    @patch('builtins.print')
    def test_opcion_1(self, mock_print):
        result = self.loop.run_until_complete(procesar_opcion(1))
        self.assertEqual(result, 1)
        mock_print.assert_called()

    @patch('builtins.print')
    def test_opcion_2(self, mock_print):
        result = self.loop.run_until_complete(procesar_opcion(2))
        self.assertEqual(result, 2)
        mock_print.assert_called()

    @patch('builtins.print')
    def test_opcion_3(self, mock_print):
        result = self.loop.run_until_complete(procesar_opcion(3))
        self.assertEqual(result, 3)
        mock_print.assert_called()

    @patch('builtins.print')
    def test_opcion_4(self, mock_print):
        result = self.loop.run_until_complete(procesar_opcion(4))
        self.assertEqual(result, 4)
        mock_print.assert_called()

    @patch('builtins.print')
    def test_opcion_5(self, mock_print):
        result = self.loop.run_until_complete(procesar_opcion(5))
        self.assertEqual(result, 5)
        mock_print.assert_called()

    @patch('builtins.print')
    def test_opcion_6_salir(self, mock_print):
        result = self.loop.run_until_complete(procesar_opcion(6))
        self.assertIsNone(result)
        mock_print.assert_called_with("Saliendo del programa...")

    @patch('builtins.print')
    def test_opcion_invalida(self, mock_print):
        result = self.loop.run_until_complete(procesar_opcion(99))
        self.assertIsNone(result)  # Mantener actual si inválida
        mock_print.assert_called_with("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    unittest.main()