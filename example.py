from pihole_api_simple import PiHole


# Create a PiHole object.  Replace http://pi.hole with the IP or hostname of your Pi-hole
client = PiHole("http://pi.hole",api_token="your-api-token-here")

# Disable Pi-hole blocking for 10 seconds
print(client.disable(duration=10))

# Enable Pi-hole blocking
print(client.enable())

# Get Pi-hole versions information
print(client.get_versions())

# Set temperature display unit (f, c or k)
print(client.set_temp_unit('f'))

# List current domains configured on Pi-hole by list type (white, black, regex_black, regex_white)
print(client.get_domain_list('black'))

# Block www.example.com on Pi-hole
print(client.update_domain_list('black','add','www.example.com'))

# Unblock www.example.com on Pi-hole
print(client.update_domain_list('black','sub','www.example.com'))

# Show cutom DNS entries
print(client.get_custom_dns())

# Add custom DNS entry
print(client.update_custom_dns('add','test.local','10.10.10.10'))

# Delete custom DNS entry
print(client.update_custom_dns('delete','test.local','10.10.10.10'))

# Show custom CNAME records
print(client.get_custom_cname())

# Add custom CNAME record
print(client.update_custom_cname('add','test.local','example.local'))

# Delete custom CNAME record
print(client.update_custom_cname('delete','test.local','example.local'))
