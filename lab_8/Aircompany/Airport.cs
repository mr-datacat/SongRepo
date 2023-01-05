using Aircompany.Models;
using Aircompany.Planes;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Aircompany
{
    public class Airport
    {
        public List<Plane> Planes { get; set; }

        public Airport(IEnumerable<Plane> planes)
        {
            Planes = planes.ToList();
        }

        public List<PassengerPlane> PassengerPlanes
        {
            get
            {
                return Planes.Where(plane => plane is PassengerPlane)
                    .Select(plane => plane as PassengerPlane).ToList();
            }
        }

        public List<MilitaryPlane> MilitaryPlanes
        {
            get
            {
                return Planes.Where(plane => plane is MilitaryPlane)
                    .Select(plane => plane as MilitaryPlane).ToList();
            }
        }

        public PassengerPlane PassengerPlaneWithMaxPassengersCapacity
        {
            get
            {
                int maxPassangersCapacity = PassengerPlanes.Max(plane => plane.PassengersCapacity);
                return PassengerPlanes.First(plane => plane.PassengersCapacity == maxPassangersCapacity);
            }
        }

        public List<MilitaryPlane> TransportMilitaryPlanes
        {
            get
            {
                return MilitaryPlanes.Where(plane => plane.Type == MilitaryType.Transport).ToList();
            }
        }

        public Airport SortByMaxDistance()
        {
            return new Airport(Planes.OrderBy(plane => plane.MaxFlightDistance));
        }

        public Airport SortByMaxSpeed()
        {
            return new Airport(Planes.OrderBy(plane => plane.MaxSpeed));
        }

        public Airport SortByMaxLoadCapacity()
        {
            return new Airport(Planes.OrderBy(plane => plane.MaxLoadCapacity));
        }

        public override string ToString()
        {
            return "Airport{" +
                    "planes=" + string.Join(", ", Planes.Select(plane => plane.Model)) +
                    '}';
        }
    }
}
