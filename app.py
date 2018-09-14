from flask import Flask, jsonify
import simplejson as json
import psycopg2
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))



conn = psycopg2.connect(dbname="ether_sql", user="postgres", password="root")
cur=conn.cursor()
cur.execute("""SELECT * FROM blocks LIMIT 10""")
columns = ('block_number', 'block_hash', 'parent_hash', 'difficulty', 'gas_used', 'miner', 'timestamp', 'sha3uncles', 'extra_data',
        'gas_limit', 'uncle_count', 'transaction_count')
results = []
for row in cur.fetchall():
        results.append(dict(zip(columns, row)))
# print(json.dumps(results, indent=2, default=json_serial))

app = Flask(__name__)

resJSON = json.dumps(results, indent=2, default=json_serial)


@app.route('/api/v1.0/all_blocks', methods=['GET'])
def get_tasks():
    return resJSON

if __name__ == '__main__':
    app.run(debug=True)