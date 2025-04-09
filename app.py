from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Get input values
    business_name = request.form['business_name']
    industry = request.form['industry']
    start_month = request.form['start_month']
    monthly_sales = float(request.form['monthly_sales'])
    other_income = float(request.form['other_income'])

    # Fixed costs
    rent = float(request.form['rent'])
    salaries = float(request.form['salaries'])
    insurance = float(request.form['insurance'])
    utilities = float(request.form['utilities'])
    depreciation = float(request.form.get('depreciation', 0))
    other_fixed_costs = float(request.form['other_fixed_costs'])

    # Variable costs
    materials_cost = float(request.form['materials_cost'])
    marketing_cost = float(request.form['marketing_cost'])
    shipping_cost = float(request.form['shipping_cost'])
    other_variable_costs = float(request.form['other_variable_costs'])

    # Tax
    tax_rate = float(request.form['tax_rate']) / 100

    # Calculations
    total_fixed_costs = rent + salaries + insurance + utilities + depreciation + other_fixed_costs
    total_variable_costs = materials_cost + marketing_cost + shipping_cost + other_variable_costs
    total_costs = total_fixed_costs + total_variable_costs

    revenue = monthly_sales + other_income
    profit_before_tax = revenue - total_costs
    tax = profit_before_tax * tax_rate
    net_profit = profit_before_tax - tax

    # Avoid divide by zero
    profit_margin = (net_profit / revenue) * 100 if revenue != 0 else 0
    break_even_sales = total_costs / (1 - tax_rate) if tax_rate < 1 else 0

    return render_template('result.html',
                           business_name=business_name,
                           industry=industry,
                           start_month=start_month,
                           total_costs=total_costs,
                           net_profit=net_profit,
                           break_even_sales=break_even_sales,
                           profit_margin=profit_margin)

if __name__ == '__main__':
    app.run(debug=True)
