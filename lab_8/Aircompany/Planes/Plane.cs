using System.Collections.Generic;

namespace Aircompany.Planes
{
    public abstract class Plane
    {
        private string _model;
        private int _maxSpeed;
        private int _maxFlightDistance;
        private int _maxLoadCapacity;

        public string Model
        {
            get { return _model; }
        }

        public int MaxSpeed
        {
            get { return _maxSpeed; }
        }

        public int MaxFlightDistance
        {
            get { return _maxFlightDistance; }
        }

        public int MaxLoadCapacity
        {
            get { return _maxLoadCapacity; }
        }

        public Plane(string model, int maxSpeed, int maxFlightDistance, int maxLoadCapacity)
        {
            _model = model;
            _maxSpeed = maxSpeed;
            _maxFlightDistance = maxFlightDistance;
            _maxLoadCapacity = maxLoadCapacity;
        }

        public override string ToString()
        {
            return "Plane{" +
                $"model='{_model}\', " +
                $"maxSpeed={_maxSpeed}, " +
                $"maxFlightDistance={_maxFlightDistance}, " +
                $"maxLoadCapacity={_maxLoadCapacity}" +
                '}';
        }

        public override bool Equals(object obj)
        {
            var plane = obj as Plane;
            return plane != null &&
                   _model == plane.Model &&
                   _maxSpeed == plane.MaxSpeed &&
                   _maxFlightDistance == plane.MaxFlightDistance &&
                   _maxLoadCapacity == plane.MaxLoadCapacity;
        }

        public override int GetHashCode()
        {
            var hashCode = -1043886837;
            hashCode = hashCode * -1521134295 + EqualityComparer<string>.Default.GetHashCode(_model);
            hashCode = hashCode * -1521134295 + _maxSpeed.GetHashCode();
            hashCode = hashCode * -1521134295 + _maxFlightDistance.GetHashCode();
            hashCode = hashCode * -1521134295 + _maxLoadCapacity.GetHashCode();
            return hashCode;
        }        

    }
}
