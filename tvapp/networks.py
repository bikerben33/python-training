# this defines available networks and streaming services
networks = ['YouTubeTV', 'YouTube', 'MAX', 'Netflix', 'Hulu', 'Disney+']
print(networks[0].title())

networks.sort()
print(networks)

for network in networks:
    print(f"Do you have {network.title()}?")

print(networks[0:3])