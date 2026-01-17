/** @param {NS} ns */
export async function main(ns) 
{
    // list of all servers
    let serverList = [];

    // recursive function to get all servers
    function allSevers(server) 
    {
        let neighbours = ns.scan(server);

        if (serverList.includes(server)) 
        {
            return;
        }

        serverList.push(server);

        for (let neighbour of neighbours) 
        {
            if (!serverList.includes(neighbour)) 
            {
                allSevers(neighbour);
            }
        }

        serverList.sort((a, b) => ns.getServerRequiredHackingLevel(a) - ns.getServerRequiredHackingLevel(b));
    }

    allSevers("home");
    
    let filename = "/logs/server-list.txt";

    ns.write(filename, "", "w");

    for(let server of serverList)
    {
        ns.write(filename, server + ": " + ns.getServerRequiredHackingLevel(server) + "\n", "o");
    } 

    ns.tprint("Server list saved to " + filename)
}