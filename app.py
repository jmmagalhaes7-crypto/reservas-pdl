from flask import Flask, render_template, request, jsonify
from datetime import datetime, date
import json
import os

app = Flask(__name__)

# File to store reservations
RESERVATIONS_FILE = 'reservations.json'

def load_reservations():
    """Load reservations from JSON file"""
    if os.path.exists(RESERVATIONS_FILE):
        with open(RESERVATIONS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_reservations(reservations):
    """Save reservations to JSON file"""
    with open(RESERVATIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(reservations, f, indent=2, ensure_ascii=False)

def validate_dates(start_date, end_date):
    """Validate that start date is before end date"""
    start = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.strptime(end_date, '%Y-%m-%d').date()
    return start <= end

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/reservations', methods=['GET'])
def get_reservations():
    """Get all reservations"""
    reservations = load_reservations()
    return jsonify(reservations)

@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    """Create a new reservation"""
    data = request.json
    
    # Validate required fields
    if not all(k in data for k in ['name', 'start_date', 'end_date']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Validate dates
    if not validate_dates(data['start_date'], data['end_date']):
        return jsonify({'error': 'Start date must be before or equal to end date'}), 400
    
    # Check for conflicts
    reservations = load_reservations()
    start = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
    end = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
    
    for res in reservations:
        res_start = datetime.strptime(res['start_date'], '%Y-%m-%d').date()
        res_end = datetime.strptime(res['end_date'], '%Y-%m-%d').date()
        
        # Check if dates overlap
        if not (end < res_start or start > res_end):
            return jsonify({'error': f'Conflict with existing reservation by {res["name"]}'}), 409
    
    # Create new reservation
    new_reservation = {
        'id': str(int(datetime.now().timestamp() * 1000)),
        'name': data['name'],
        'start_date': data['start_date'],
        'end_date': data['end_date'],
        'notes': data.get('notes', ''),
        'created_at': datetime.now().isoformat()
    }
    
    reservations.append(new_reservation)
    save_reservations(reservations)
    
    return jsonify(new_reservation), 201

@app.route('/api/reservations/<reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    """Delete a reservation"""
    reservations = load_reservations()
    original_count = len(reservations)
    reservations = [r for r in reservations if r['id'] != reservation_id]
    
    if len(reservations) == original_count:
        return jsonify({'error': 'Reservation not found'}), 404
    
    save_reservations(reservations)
    return jsonify({'message': 'Reservation deleted'}), 200

@app.route('/api/reservations/<reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    """Update a reservation"""
    data = request.json
    reservations = load_reservations()
    
    # Find reservation
    reservation = None
    for r in reservations:
        if r['id'] == reservation_id:
            reservation = r
            break
    
    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404
    
    # Validate dates if provided
    start_date = data.get('start_date', reservation['start_date'])
    end_date = data.get('end_date', reservation['end_date'])
    
    if not validate_dates(start_date, end_date):
        return jsonify({'error': 'Start date must be before or equal to end date'}), 400
    
    # Check for conflicts (excluding current reservation)
    start = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.strptime(end_date, '%Y-%m-%d').date()
    
    for res in reservations:
        if res['id'] == reservation_id:
            continue
        
        res_start = datetime.strptime(res['start_date'], '%Y-%m-%d').date()
        res_end = datetime.strptime(res['end_date'], '%Y-%m-%d').date()
        
        if not (end < res_start or start > res_end):
            return jsonify({'error': f'Conflict with existing reservation by {res["name"]}'}), 409
    
    # Update reservation
    reservation.update({
        'name': data.get('name', reservation['name']),
        'start_date': start_date,
        'end_date': end_date,
        'notes': data.get('notes', reservation.get('notes', ''))
    })
    
    save_reservations(reservations)
    return jsonify(reservation), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

