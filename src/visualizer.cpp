#include "visualizer.h"

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;
typedef visualization_msgs::MarkerArray MarkerArray;

Visualizer::Visualizer(double marker_lifetime)
{
	this->marker_lifetime = marker_lifetime;
}

MarkerArray 
Visualizer::createCylinders(const std::vector<CylindricalShell> &list, const std::string &frame)
{
  // create and resize a marker array message
	MarkerArray marker_array;
	marker_array.markers.resize(list.size());
			
	for (int i = 0; i < list.size(); i++)
	{				
		// create marker
		visualization_msgs::Marker marker;
		marker.header.frame_id = frame;
		marker.header.stamp = ros::Time::now();
		
		// namespace and id to give the marker a unique identification
		marker.ns = "cylinders_ns";
		marker.id = i;
		
		// how long the marker exists
		marker.lifetime = ros::Duration(this->marker_lifetime);
		
		// type of marker (cylinder)
		marker.type = visualization_msgs::Marker::CYLINDER;
		marker.action = visualization_msgs::Marker::ADD;
		
		// marker position
		marker.pose.position.x = list[i].getCentroid()(0);
		marker.pose.position.y = list[i].getCentroid()(1);
		marker.pose.position.z = list[i].getCentroid()(2);
		
		// marker rotation
		geometry_msgs::PoseStamped cylinder_pose_msg;
		Eigen::Vector3d axis = list[i].getCurvatureAxis();
		Eigen::Vector3d normal = list[i].getNormal();
		Eigen::Vector3d perp = normal.cross(axis);
		tf::Matrix3x3 rotation_matrix(perp(0), normal(0), axis(0), 
								perp(1), normal(1), axis(1), 
								perp(2), normal(2), axis(2));
		tf::Quaternion quaternion;
		rotation_matrix.getRotation(quaternion);
		tf::Stamped<tf::Transform> cylinder_tf_pose(tf::Transform(quaternion), marker.header.stamp, frame);
		tf::poseStampedTFToMsg(cylinder_tf_pose, cylinder_pose_msg);					
		marker.pose.orientation = cylinder_pose_msg.pose.orientation;
		
		// marker scale
		marker.scale.x = list[i].getRadius() * 2; // diameter in x-direction
		marker.scale.y = list[i].getRadius() * 2; // diameter in y-direction 
		marker.scale.z = list[i].getExtent(); // height
		
		// marker color and transparency
		marker.color.a = 0.3;
		marker.color.r = 0;
		marker.color.g = 255;
		marker.color.b = 255;
		
		marker_array.markers[i] = marker;
	}
	
	return marker_array;  
}

void 
Visualizer::createHandles(const std::vector< std::vector<CylindricalShell> > &handles, 
                          const std::string &frame, std::vector<MarkerArray> &marker_arrays, 
                          MarkerArray &all_handle_markers)
{
  marker_arrays.resize(handles.size());
  std::vector<CylindricalShell> handle_shells;
  int k = 0;
  
	for (int i=0; i < handles.size(); i++)
  {
    marker_arrays[i] = this->createCylinders(handles[i], frame);
    for (int j=0; j < handles[i].size(); j++)
        handle_shells.push_back(handles[i][j]);
  }
  
  all_handle_markers = this->createCylinders(handle_shells, frame);
}
