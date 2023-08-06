Plot4GMNS: A visualization tool for visualizing and analyzing transportation network based on GMNS data format
==============================================================================================================

Introduction
------------

Plot4GMNS is an open-source transportation network data visualization
and analysis tool based on GMNS data format. By taking advantage of
OSM2GMNS and Grid2demand tools to obtain routable transportation network
and demand, Plot4GMNS aims to visualize and analyze the node, link, POI,
agent, and zone data of the network.

Installation
------------

::

    pip install plot4gmns

Simple Example
--------------

.. code:: python

    >>>import plot4gmns as pg
    """
    Step 1: build network from csv files:
        node.csv,link.csv,poi.csv(output by osm2gmns);
        input_agent.csv,zone.csv,demand.csv,poi_trip_rate.csv(output by grid2demand)
    """
    >>>net=pg.readNetwork('./data')

    """Step 2: check vaild network  attributes"""
    >>>net.get_valid_node_attr_list() #node attributes
        attr                          type                
        ctrl_type                     int                 
        activity_type                 str                 
        production                    float               
        attraction                    float  
    >>>net.get_valid_link_attr_list() #link attributes
        attr                          type                
        length                        float               
        lanes                         int                 
        free_speed                    float               
        capacity                      float               
        link_type_name                str                 
        allowed_uses                  str   
    >>>net.get_valid_poi_attr_list() #poi attributes
        attr                          type                
        building                      str                 
        activity_zone_id              int    
    >>>net.get_valid_zone_id_list() #zone attributes
        min zone id         max zone id         
        1                   45      

    """Step 3: get network attributes value list"""
    >>>pg.get_node_attr_value_list(net,'activity_type')
        activity_type       number              
        primary             455                 
        residential         273                 
        tertiary            17                  
        unclassified        173                 
        secondary           33                  
        footway             2                   
        poi                 1818                
        centroid node       45 
    >>>pg.get_link_attr_value_list(net,'link_type_name')
        link_type_name      number              
        unclassified        329                 
        primary             764                 
        secondary           69                  
        residential         583                 
        tertiary            21                  
        footway             1                   
        connector           3636  
    >>>pg.get_poi_attr_value_list(net,'building')
        building                      number              
        train_station                 10                  
        theatre                       8                   
        yes                           1158                
        court_yard                    1                   
        museum                        1                   
        block                         2                   
        flats                         6                   
        apartments                    126 
        ...                           ...
    >>>pg.get_zone_id_list(net,zone_id=1)
        zone_id             name                total_poi_count     total_production    total_attraction    
        1                   A1                  96.0                837.1866378514361   588.2430837535613   

    """Step 4: show network of different modes"""
    >>>pg.showNetByAllMode(net) #all modes
    ![ ](all_mode.png)

    >>>pg.showNetByAutoMode(net) # auto mode
    ![ ](auto_mode.png)

    >>>pg.showNetByRailMode(net) # rail mode
    ![ ](rail.png)

    """Step 5: show network by node attribute"""
    >>>pg.showNetByNodeAttr(net,{'activity_type':'primary'})
    ![ ](node_activity_type.png)

    >>>pg.showNetByNodeAttr(net,{'attraction':(0.001,0.08)})
    ![ ](node_attraction.png)

    >>>pg.showNetByNodeProduction(net)
    ![ ](node_production.png)

    """Step 6: show network by link attribute"""
    >>>pg.showNetByLinkAttr(net,{'link_type_name':'secondary'})
    ![ ](link_type_name.png)

    >>>pg.showNetByLinkFreeSpeed(net)
    ![ ](free_speed.png)

    """Step 7 : show network by poi attribute"""
    >>>pg.showNetByPOIAttr(net,{'activity_zone_id':(1,5)})
    ![ ](poi_activity_zone_id.png)

    >>>pg.showNetByPOIAttractionHeat(net)
    ![ ](poi_attraction_heat.png)

    >>>pg.showNetByPOIAttractionContour(net)
    ![ ](poi_attraction_contour.png)

    """Step 8: show network by zone attribute"""
    >>>pg.showNetByZoneDemandHeat(net,annot=False)
    ![ ](zone_demand_heat.png)

    >>>pg.showNetByZoneDemandFlow(net,annot=True,bg=True)
    ![ ](zone_demand_flow.png)

    >>>pg.showNetByZoneAgent(net,[(1,15),(16,5)])
    ![ ](zone_agent.png)

User guide
----------

Users can check the `user guide <>`__ for detialed introduction of
plot4gmns.
