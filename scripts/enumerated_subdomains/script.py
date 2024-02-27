import sys, dns.resolver

def enum_subdomains(domain, wordlist):
    resolver = dns.resolver.Resolver()

    try:
        with open(wordlist, "r") as arq:
            subdomains = arq.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{wordlist}' not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    for subdomain in subdomains:
        try:
            target = f"{subdomain}.{domain}"
            results = resolver.resolve(target, "A")
            for result in results:
                print(f"{target} -> {result}")
        except dns.resolver.NoAnswer:
            print(f"No DNS records found for '{target}'")
        except dns.resolver.NXDOMAIN:
            print(f"DNS domain '{target}' does not exist")
        except dns.resolver.NoNameservers:
            print(f"No nameservers found")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <domain> <wordlist>")
        sys.exit()

    domain = sys.argv[1]
    wordlist = sys.argv[2]
    enum_subdomains(domain, wordlist)