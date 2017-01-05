melon_cost = 1.00


def expected_vs_paid(customer_name, customer_melons, customer_paid):
    customer_expected = int(customer_melons) * melon_cost
    customer_paid = float(customer_paid)
    if customer_expected != customer_paid:
        print customer_name + " paid " + str(customer_paid) + ", expected " + str(customer_expected)

the_file = open("customer-orders.txt")
for line in the_file:
    line = line.strip()
    words = line.split('|')

    customer_name = words[1]
    customer_melons = words[2]
    customer_paid = words[3]

    print expected_vs_paid(customer_name,customer_melons,customer_paid)