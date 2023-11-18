import asyncio
import unittest
import uuid
import os
from falconai import models_get, model_post, model_patch, model_delete


class TestModelLifecycle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Generate a unique model name for use in all tests
        cls.model_name = f"test_{uuid.uuid4()}"
        cls.external_uid = None
        os.environ["FALCON_API_KEY"] = "eyJraWQiOiJvMU5OWE1jNmtOS29qN1BoekV4NjZCQUZSWFZZblRCbllQVkJLbldhUWg4PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJhZjZmNDk5ZS1kYTMyLTRjODYtOTE0ZC1hMjRkNWJhOTE2NTgiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9WMjhONTZtbmciLCJjbGllbnRfaWQiOiIyaHNoamdobWxxMnVmM2gyMGtoNmd2dmx0aCIsIm9yaWdpbl9qdGkiOiIwOTM5Y2E5Mi0yMzIxLTRlZDYtODlhZC0yZDQ5ZGQ0OWYzYWUiLCJldmVudF9pZCI6ImViMzkyYjcyLTBkZmItNDBhYi04NzUxLTY0NDEzZGVkMTdmMyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2OTg4NTk2NjIsImV4cCI6MTY5ODg2MzI2MiwiaWF0IjoxNjk4ODU5NjYyLCJqdGkiOiI2OTA4ZTAwMy0zOTM3LTQzNzYtYThjYi05OWZhMDcxOTc2YTEiLCJ1c2VybmFtZSI6ImFmNmY0OTllLWRhMzItNGM4Ni05MTRkLWEyNGQ1YmE5MTY1OCJ9.tinmlf7hGT5nBuH0KKulw7ukhX46kNJRnykpP-fJs8fzUqbCGy2RVyASH2n3ib3aRXSLLY1EjnaEeFvLBUx9lowRiuRD1ivQQoxjhrIvGaxhAAavnl96Yl2BZqjXlPWawW8rozsr0GmmJLGVeLfc88B1f9qTB0YopRA5m5oUCJzB-x-g0DANyB5GFMS5n278FO9YV-HHIlj36uw1d47mvtfgYSgrZITxOcTQHLsftOdoeV9xEeMFZipwE7xHcCOpClBOgu5BGXNuimaMaGrKJTcHr8nZ6aKP4l-octUEYxCBSirEpJZYlQLdmCb6rX_qywxV8mnt7XbYNrBYl46mlQ"

        

    def setUp(self):
        # # Create model and set external_uid for each test
        # create_response = asyncio.run(model_post(
        #     model_name=self.model_name,
        #     # ... other parameters
        # ))
        # self.external_uid = create_response.get('data', {}).get('external_uid')
        pass

    def tearDown(self):
        # # Delete model after each test
        # if self.external_uid:
        #     asyncio.run(model_delete(external_uid=self.external_uid))
        pass
    
    def run_async_test(self, coro):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(coro)
        loop.close()
        return result


    def test_1_model_create_and_confirm(self):
        async def run_test():
            # Step 1: Create the model
            create_response = await model_post(
                model_name=self.model_name,
                model_type="base",
                version="1.0",
                year=2021,
                dataset_size="large",
                provider="provider_name",
                modality="text",
                max_tokens="512",
                description="Test model",
                model_attributes="attributes"
            )
            self.assertEqual(create_response.get('status_code'), 200, "Failed to create model")
            create_data = create_response.get('data', {})
            self.assertIn('external_uid', create_data, "Response data does not contain 'external_uid'")
            self.external_uid = create_data['external_uid']
            TestModelLifecycle.external_uid = create_data['external_uid']


            # Step 2: Confirm creation using models_get
            list_response = await models_get()
            self.assertIn(self.external_uid, [model.get('external_uid') for model in list_response.get('data', [])], 
                        f"Model with UID '{self.external_uid}' not found in models list")
         
        self.run_async_test(run_test())


    def test_2_model_patch_and_confirm(self):
        async def run_test():
            # Step 3: Patch (update) the model with new values
            patch_data = {
                'version': '2.0',
                'provider': 'updated_provider'
            }
            patch_response = await model_patch(
                id=TestModelLifecycle.external_uid,
                **patch_data
            )
            self.assertEqual(patch_response.get('status_code'), 200, "Failed to patch model")

            # Step 4: Confirm update by retrieving the updated model
            list_response = await models_get()
            updated_model = next((model for model in list_response.get('data', []) 
                                if model.get('external_uid') == TestModelLifecycle.external_uid), None)
            self.assertIsNotNone(updated_model, "Updated model not found")

            # Check if the fields were updated correctly
            for key, value in patch_data.items():
                self.assertEqual(updated_model.get(key), value, f"Field {key} was not updated correctly")
        
        self.run_async_test(run_test())



    def test_3_model_delete_and_confirm(self):
        async def run_test():
            # Step 5: Delete the model
            delete_response = await model_delete(id=TestModelLifecycle.external_uid)
            self.assertEqual(delete_response.get('status_code'), 200, "Failed to delete model")

            # Step 6: Confirm deletion using models_get
            list_response = await models_get()
            self.assertNotIn(TestModelLifecycle.external_uid, [model['external_uid'] for model in list_response.get('data', [])], 
                            "Model was not deleted")
        
        self.run_async_test(run_test())

if __name__ == '__main__':
    unittest.main()
