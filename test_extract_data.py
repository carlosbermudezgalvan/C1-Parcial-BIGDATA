import json
import unittest
from unittest.mock import Mock, patch
from extract_data import lambda_handler_processing  # Importa tu función aquí

class TestLambdaHandlerProcessing(unittest.TestCase):
    @patch('extract_data.boto3.client')
    @patch('extract_data.boto3.resource')
    def test_lambda_handler_processing(self, mock_boto3_resource, mock_boto3_client):
        # Simular el comportamiento de boto3
        mock_s3_resource = Mock()
        mock_boto3_resource.return_value = mock_s3_resource
        mock_s3_client = Mock()
        mock_boto3_client.return_value = mock_s3_client
        mock_s3_object = Mock()
        mock_s3_resource.Object.return_value = mock_s3_object
        mock_s3_object.get.return_value = {'Body': Mock(read=Mock(return_value=b"Contenido HTML"))}
        
        # Ejecutar la función bajo prueba
        result = lambda_handler_processing(None, None)
        
        # Verificar llamadas y comportamiento
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(mock_s3_client.put_object.call_count, 2)  # Se debe llamar dos veces
        
        # ... otras aserciones si es necesario ...

if __name__ == '__main__':
    unittest.main()
