from datetime import datetime, timedelta

BUCKET = 'tee_lskd_lskkja'
MEASUREMENT = "test"
DEVICE_ID = "test.ch"
N_SAMPLES = 10239
TEST_DATA = {
    "measurement": MEASUREMENT,
    "device_id": DEVICE_ID,
    "values": [(datetime.now() - timedelta(minutes=i), i) for i in range(0, N_SAMPLES)]
}


def test_deviceid_count(client):
    client.save_data(bucket=BUCKET, data=TEST_DATA)
    count = client.bucket_data_count(bucket=BUCKET)
    assert count['total_count'] == N_SAMPLES
    assert count['devices_count'] == {DEVICE_ID: N_SAMPLES}
