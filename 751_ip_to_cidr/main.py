class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # In its binary form, count the number of trailing zeros.
        def count_trailing_zeros(num):
            # Find the largest power of 2 that divides num
            power = 0
            limit = 32 # max bits in ip addr
            while num % (2 ** power) == 0:
                power += 1
                if power > limit:
                    break
            
            return power - 1
        
        def num_to_ip(num):
            # Determine the 4 blocks of 256
            a = num // (256 ** 3)
            b = (num // (256 ** 2)) % 256
            c = (num // 256) % 256
            d = num % 256
            return f"{a}.{b}.{c}.{d}"
        
        # Return a list of cidr blocks starting from num and cover
        # block_size number of ip addresses
        def num_to_cidr(num, block_size):
            # Each mask represents a power of 2 so we must take
            # powers of 2 from block_size each time
            power = floor(math.log2(block_size))
            result = []
            while block_size > 0:
                if 2 ** power > block_size:
                    power -= 1
                    continue
                
                result.append(num_to_ip(num) + "/" + str(32 - power))

                num += 2 ** power
                block_size -= 2 ** power
                power -= 1


            return result


        # Turn the ip addr to a number
        parts = ip.split(".")
        num = int(parts[0]) * (256 ** 3) + int(parts[1]) * (256 ** 2) + int(parts[2]) * (256 ** 1) + int(parts[3])

        result = []
        while n > 0:
            trailing_zeros = count_trailing_zeros(num)
            take = min(2 ** trailing_zeros, n)
            
            result.extend(num_to_cidr(num, take))

            n -= take
            num += take


        return result
        
