#I want to create a bandwidth monitor

#Useful libraries that I would be working with -->
import os
import time
import psutil

#Declaring the function
def monitor(time_ = 30):
    lastReceived = psutil.net_io_counters().bytes_recv
    lastSent = psutil.net_io_counters().bytes_sent
    lastTotal = lastReceived + lastSent
    stats = f"""{'~' * 30} BANDWIDTH MONITOR REPORT {'~' * 30}
    
\tSECONDS\t|\tRECEIVED DATA\t|\tSENT DATA\t|\tTOTAL DATA\t\n{'~' * 100}\n"""
    
    id = 1
    while True:
        bytesReceived = psutil.net_io_counters().bytes_recv
        bytesSent = psutil.net_io_counters().bytes_sent
        bytesTotal = bytesReceived + bytesSent

        newReceived = bytesReceived - lastReceived
        newSent = bytesSent - lastSent
        newTotal = bytesTotal - lastTotal

        mbNewReceived = newReceived / 1024 / 1024
        mbNewSent = newSent / 1024 / 1024
        mbNewTotal = newTotal / 1024 / 1024

        stats += f"\t{id}\t|\t{mbNewReceived:.2f} MB\t\t|\t{mbNewSent:.2f} MB\t\t|\t{mbNewTotal:.2f} MB\t\t\n"
        #print(f"    {id}    |  {mbNewReceived:.2f} MB     |   {mbNewSent:.2f} MB     |   {mbNewTotal:.2f} MB    \n")

        lastReceived = bytesReceived
        lastSent = bytesSent
        lastTotal = bytesTotal
        id += 1

        time.sleep(1)
        if id == time_ + 1:
            break
    return stats
        
         

if __name__ == "__main__":
    print("BANDWIDTH MONITOR \n")

    secs = 50
    stats = monitor(secs)
    print(stats)

    print("\nExecuted successfully!")
